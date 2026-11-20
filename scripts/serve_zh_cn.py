"""Serve the checked-out Chinese curriculum on a loopback HTTP address."""

import argparse
import io
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import quote, unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
HOME = "/zh-CN/README.md"
READABLE_ROOTS = {
    "zh-CN", "phases", "manuals", "projects", "certifications", "interviews",
    "practice", "cheatsheets", "glossary", "learning-paths", "assets", "outputs",
    "docs", "skills", "book", "i18n",
}
ROOT_FILES = {"README.md", "ROADMAP.md", "LICENSE", "CONTRIBUTING.md"}
MATH_BLOCK = re.compile(r"(?m)^\x60{3}math[ \t]*\n(.+?)^\x60{3}[ \t]*$", re.S)
PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{ color-scheme: light dark; --accent: light-dark(#126354, #8cdecc); }}
body {{ margin: 0; font: 17px/1.75 system-ui, "Microsoft YaHei", sans-serif; }}
header {{ border-bottom: 1px solid GrayText; }}
nav, main {{ max-width: 70ch; margin: auto; padding: .9rem 1.15rem; }}
nav {{ display: flex; gap: .7rem 1.4rem; flex-wrap: wrap; font-size: .94rem; }}
main {{ padding-bottom: 4rem; overflow-wrap: anywhere; }}
h1, h2, h3 {{ line-height: 1.28; }}
h1 {{ margin: 1rem 0 1.4rem; }}
h2 {{ margin-top: 2rem; }}
a {{ color: var(--accent); text-underline-offset: .15em; }}
img {{ max-width: 100%; height: auto; }}
pre, table, math[display=block] {{ max-width: 100%; overflow: auto; }}
pre {{ background: light-dark(#f2f4f2, #242823); border-radius: .45rem; padding: 1rem; line-height: 1.5; }}
table {{ display: block; border-collapse: collapse; }}
th, td {{ border: 1px solid GrayText; padding: .45rem .65rem; }}
blockquote {{ border-inline-start: .25rem solid var(--accent); padding-inline-start: 1rem; margin-inline: 0; }}
summary {{ color: var(--accent); cursor: pointer; }}
details {{ padding: .45rem .75rem; border: 1px solid GrayText; border-radius: .4rem; }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 3px; }}
</style>
</head>
<body>
<header><nav aria-label="课程导航"><a href="/zh-CN/README.md">中文课程</a>
<a href="/zh-CN/ROADMAP.md">路线图</a>
<a href="/zh-CN/glossary/terms.md">中英术语表</a></nav></header>
<main>{body}</main>
</body>
</html>
"""


class Reader(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'none'; style-src 'unsafe-inline'; img-src 'self' https: data:; "
            "base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
        )
        super().end_headers()

    def send_head(self):
        port = self.server.server_port
        if self.headers.get("Host") not in {f"127.0.0.1:{port}", f"localhost:{port}"}:
            self.send_error(403)
            return None
        try:
            url = urlsplit(self.path)
            decoded = unquote(url.path, errors="strict")
        except (UnicodeError, ValueError):
            self.send_error(400)
            return None
        if decoded == "/":
            self.send_response(302)
            self.send_header("Location", HOME)
            self.end_headers()
            return None
        parts = decoded.strip("/").split("/")
        if (
            not decoded.startswith("/") or url.netloc or url.scheme
            or any(not part or part.startswith(".") or any(c in part for c in ":\\\0") for part in parts)
            or (parts[0] not in READABLE_ROOTS and not (len(parts) == 1 and parts[0] in ROOT_FILES))
        ):
            self.send_error(404)
            return None
        target = ROOT.joinpath(*parts).resolve()
        if target != ROOT.joinpath(*parts) or not target.is_relative_to(ROOT):
            self.send_error(404)
            return None
        if target.is_dir() and (target / "README.md").is_file():
            destination = "/" + "/".join(quote(part) for part in parts) + "/README.md"
            self.send_response(302)
            self.send_header("Location", destination)
            self.end_headers()
            return None
        if target.is_file() and target.suffix.lower() == ".md":
            return self.render_markdown(target, parts[0] == "zh-CN")
        return super().send_head()

    def render_markdown(self, target, chinese):
        try:
            markdown = target.read_text(encoding="utf-8-sig")
            markdown = MATH_BLOCK.sub(lambda m: "\n$$\n" + m[1] + "$$\n", markdown)
            result = subprocess.run(
                [self.server.pandoc, "--from=gfm+tex_math_dollars", "--to=html5", "--mathml"],
                input=markdown,
                capture_output=True,
                encoding="utf-8",
                check=True,
                timeout=15,
            )
        except (OSError, UnicodeError, subprocess.SubprocessError):
            self.send_error(500, "Markdown rendering failed")
            return None
        page = PAGE.format(
            lang="zh-CN" if chinese else "en",
            title="从零开始学 AI 工程",
            body=result.stdout,
        ).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        return io.BytesIO(page)

    def translate_path(self, request_path):
        return str(ROOT / unquote(urlsplit(request_path).path).lstrip("/"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--pandoc", default="pandoc", help="Pandoc executable name or path")
    args = parser.parse_args()
    pandoc = shutil.which(args.pandoc)
    if not pandoc:
        parser.error("Pandoc executable not found. https://pandoc.org/installing.html")
    with ThreadingHTTPServer(("127.0.0.1", args.port), Reader) as server:
        server.pandoc = pandoc
        print(f"http://127.0.0.1:{server.server_port}/", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
