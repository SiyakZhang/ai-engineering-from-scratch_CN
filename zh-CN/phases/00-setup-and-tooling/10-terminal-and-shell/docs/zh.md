# 终端与 Shell

> 终端是 AI 工程师生活的地方。在这儿待舒服点。

**类型：** Learn（概念学习）
**语言：** --
**前置要求：** 阶段 0，第 1 课
**预计时间：** ~35 分钟

## 学习目标

- 用管道、重定向和 `grep` 在命令行里过滤和处理训练日志
- 创建带多个窗格的持久化 tmux 会话，同时跑训练和 GPU（图形处理器） 监控
- 用 `htop`、`nvtop` 和 `nvidia-smi` 监控系统和 GPU 资源
- 用 SSH、`scp` 和 `rsync` 在本地和远程机器之间传文件

## 问题背景

你待在终端里的时间会比待在任何编辑器里都长。训练任务、GPU 监控、日志跟踪、远程 SSH 会话、环境管理。每个 AI 工作流都要碰 shell。你在这儿慢，你哪儿都慢。

这节课讲对 AI 工作要紧的终端技能。没有 Unix 历史。没有 Bash 脚本的深挖。只讲你需要的。

## 核心概念

```mermaid
graph TD
    subgraph tmux["tmux 会话: training"]
        subgraph top["上半部分"]
            P1["窗格 1: 训练任务<br/>python train.py<br/>Epoch 12/100 ..."]
            P2["窗格 2: GPU 监控<br/>watch -n1 nvidia-smi<br/>GPU: 78% | Mem: 14/24G"]
        end
        P3["窗格 3: 日志 + 实验<br/>tail -f logs/train.log | grep loss"]
    end
```

三样东西同时跑。一个终端。你可以分离（detach）、回家、再 SSH 回来、重新接上（reattach）。训练一直在跑。

```figure
s0-shell-pipeline
```

## 动手构建

### 第 1 步：了解你的 shell

看看你跑的是哪个 shell：

```bash
echo $SHELL
```

大多数系统用 `bash` 或 `zsh`。两个都行。本课程的命令在哪个里都能跑。

需要知道的要点：

```bash
# Move around
cd ~/projects/ai-engineering-from-scratch
pwd
ls -la

# History search (most useful shortcut you'll learn)
# Ctrl+R then type part of a previous command
# Press Ctrl+R again to cycle through matches

# Clear terminal
clear   # or Ctrl+L

# Cancel a running command
# Ctrl+C

# Suspend a running command (resume with fg)
# Ctrl+Z
```

### 第 2 步：管道和重定向

管道把命令连在一起。这就是你处理日志、过滤输出、串联工具的方式。你会一直用它。

```bash
# Count how many times "loss" appears in a log
cat train.log | grep "loss" | wc -l

# Extract just the loss values from training output
grep "loss:" train.log | awk '{print $NF}' > losses.txt

# Watch a log file update in real time, filtering for errors
tail -f train.log | grep --line-buffered "ERROR"

# Sort experiments by final accuracy
grep "final_accuracy" results/*.log | sort -t= -k2 -n -r

# Redirect stdout and stderr to separate files
python train.py > output.log 2> errors.log

# Redirect both to the same file
python train.py > train_full.log 2>&1
```

你需要掌握四种重定向和一种管道：

| 符号 | 它干什么 |
|--------|-------------|
| `>` | 把 stdout 写入文件（覆盖） |
| `>>` | 把 stdout 追加到文件 |
| `2>` | 把 stderr 写入文件 |
| `2>&1` | 把 stderr 送到 stdout 所去的同一个地方 |
| `\|` | 把一个命令的 stdout 作为下一个命令的 stdin |

### 第 3 步：后台进程

训练任务要跑好几个小时。你不会想全程开着终端。

```bash
# Run in background (output still goes to terminal)
python train.py &

# Run in background, immune to hangup (closing terminal won't kill it)
nohup python train.py > train.log 2>&1 &

# Check what's running in background
jobs
ps aux | grep train.py

# Bring a background job to foreground
fg %1

# Kill a background process
kill %1
# or find its PID and kill that
kill $(pgrep -f "train.py")
```

`&`、`nohup` 和 `screen`/`tmux` 的区别：

| 方法 | 终端关了还活着吗？ | 能重新接上吗？ |
|--------|-------------------------|---------------|
| `command &` | 否 | 否 |
| `nohup command &` | 是 | 否（看日志文件） |
| `screen` / `tmux` | 是 | 是 |

任何超过几分钟的东西，都用 tmux。

### 第 4 步：tmux

tmux 让你创建带多个窗格的持久化终端会话。这是管理训练任务最有用的单个工具。

```bash
# Install
# macOS
brew install tmux
# Ubuntu
sudo apt install tmux

# Start a named session
tmux new -s training

# Split horizontally
# Ctrl+B then "

# Split vertically
# Ctrl+B then %

# Navigate between panes
# Ctrl+B then arrow keys

# Detach (session keeps running)
# Ctrl+B then d

# Reattach
tmux attach -t training

# List sessions
tmux ls

# Kill a session
tmux kill-session -t training
```

一个典型的 AI 工作流会话：

```bash
tmux new -s train

# Pane 1: start training
python train.py --epochs 100 --lr 1e-4

# Ctrl+B, " to split, then run GPU monitor
watch -n1 nvidia-smi

# Ctrl+B, % to split vertically, tail the logs
tail -f logs/experiment.log

# Now detach with Ctrl+B, d
# SSH out, go get coffee, come back
# tmux attach -t train
```

### 第 5 步：用 htop 和 nvtop 监控

```bash
# System processes (better than top)
htop

# GPU processes (if you have NVIDIA GPU)
# Install: sudo apt install nvtop (Ubuntu) or brew install nvtop (macOS)
nvtop

# Quick GPU check without nvtop
nvidia-smi

# Watch GPU usage update every second
watch -n1 nvidia-smi

# See which processes are using the GPU
nvidia-smi --query-compute-apps=pid,name,used_memory --format=csv
```

你会用到的 `htop` 快捷键：
- `F6` 或 `>` 按列排序（按内存排序找内存泄漏）
- `F5` 切换树状视图（看子进程）
- `F9` 杀掉一个进程
- `/` 搜索进程名

### 第 6 步：用 SSH 连远程 GPU 机器

你租一块云 GPU 时（Lambda、RunPod、Vast.ai），通过 SSH 连接。

```bash
# Basic connection
ssh user@gpu-box-ip

# With a specific key
ssh -i ~/.ssh/my_gpu_key user@gpu-box-ip

# Copy files to remote
scp model.pt user@gpu-box-ip:~/models/

# Copy files from remote
scp user@gpu-box-ip:~/results/metrics.json ./

# Sync a whole directory (faster for many files)
rsync -avz ./data/ user@gpu-box-ip:~/data/

# Port forward (access remote Jupyter/TensorBoard locally)
ssh -L 8888:localhost:8888 user@gpu-box-ip
# Now open localhost:8888 in your browser

# SSH config for convenience
# Add to ~/.ssh/config:
# Host gpu
#     HostName 192.168.1.100
#     User ubuntu
#     IdentityFile ~/.ssh/gpu_key
#
# Then just:
# ssh gpu
```

### 第 7 步：AI 工作好用的别名（alias）

把这些加进你的 `~/.bashrc` 或 `~/.zshrc`：

```bash
source phases/00-setup-and-tooling/10-terminal-and-shell/code/shell_aliases.sh
```

或者挑你想要的复制走。关键的别名：

```bash
# GPU status at a glance
alias gpu='nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total,temperature.gpu --format=csv,noheader'

# Kill all Python training processes
alias killtraining='pkill -f "python.*train"'

# Quick virtual environment activate
alias ae='source .venv/bin/activate'

# Watch training loss
alias watchloss='tail -f logs/*.log | grep --line-buffered "loss"'
```

完整的一套见 `code/shell_aliases.sh`。

### 第 8 步：常见的 AI 终端套路

这些在实践中反复出现：

```bash
# Run training, log everything, notify when done
python train.py 2>&1 | tee train.log; echo "DONE" | mail -s "Training complete" you@email.com

# Compare two experiment logs side by side
diff <(grep "accuracy" exp1.log) <(grep "accuracy" exp2.log)

# Find the largest model files (clean up disk space)
find . -name "*.pt" -o -name "*.safetensors" | xargs du -h | sort -rh | head -20

# Download a model from Hugging Face
wget https://huggingface.co/model/resolve/main/model.safetensors

# Untar a dataset
tar xzf dataset.tar.gz -C ./data/

# Count lines in all Python files (see how big your project is)
find . -name "*.py" | xargs wc -l | tail -1

# Check disk space (training data fills disks fast)
df -h
du -sh ./data/*

# Environment variable check before training
env | grep -i cuda
env | grep -i torch
```

## 实际使用

本课程里每个工具什么时候派上用场：

| 工具 | 你什么时候用它 |
|------|----------------|
| tmux | 每次训练任务（阶段 3 及以后） |
| `tail -f` + `grep` | 监控训练日志 |
| `nohup` / `&` | 快速的后台任务 |
| `htop` / `nvtop` | 调试训练变慢、OOM 错误 |
| SSH + `rsync` | 在云 GPU 上干活 |
| 管道 + 重定向 | 处理实验结果 |
| 别名 | 在重复命令上省时间 |

## 练习

1. 装上 tmux，创建一个带三个窗格的会话，一个里跑 `htop`，另一个跑 `watch -n1 date`，第三个跑一个 Python 脚本。分离再重新接上。
2. 把 `code/shell_aliases.sh` 里的别名加进你的 shell 配置，用 `source ~/.zshrc`（或 `~/.bashrc`）重新加载。
3. 用 `for i in $(seq 1 100); do echo "epoch $i loss: $(echo "scale=4; 1/$i" | bc)"; sleep 0.1; done > fake_train.log` 造一份假训练日志，然后用 `grep`、`tail` 和 `awk` 只抽出 loss 值。
4. 为一台你有权限的服务器配一条 SSH config 条目（或用 `localhost` 来练语法）。

### 提示

**练习 1。** 先运行 `tmux new -s practice`，用前缀 `Ctrl+B` 后接 `"` 和 `%` 分屏，再用 `Ctrl+B` 和方向键切换面板。按 `Ctrl+B`、`d` 脱离会话，运行 `tmux ls`，再用 `tmux attach -t practice` 重新连接；三个程序都应仍在运行。

**练习 2。** 将 `code/shell_aliases.sh` 中的行复制到 `~/.zshrc` 或 `~/.bashrc` 末尾，对该文件执行 `source`。用 `alias` 或 `type <name>` 检查一个新别名，确认 shell 已识别它。

**练习 3。** 先运行 `tail -5 fake_train.log` 查看行格式，再用 `grep loss` 筛选，并通过 `awk '{print $NF}'` 只输出最后一列。结果应是 100 个逐渐减小的数字。

**练习 4。** 将课程中的 `Host gpu` 块复制到 `~/.ssh/config`，把 `HostName` 和 `User` 改为你的服务器信息，或改为 `localhost` 和本机用户名。运行 `ssh -G gpu` 输出实际使用的设置。如果有可访问且接受你密钥的 SSH 服务，再运行 `ssh gpu` 连接。

## 关键术语

| 术语 | 大家口头怎么说 | 它实际指什么 |
|------|----------------|----------------------|
| Shell | "终端" | 解释你命令的程序（bash、zsh、fish） |
| tmux | "终端复用器" | 一个程序，让你在一个窗口里跑多个终端会话，并能分离/重新接上 |
| 管道（Pipe） | "那个竖杠" | `\|` 操作符，把一个命令的输出作为另一个命令的输入 |
| PID | "进程 ID" | 分配给每个运行中进程的唯一编号，用来监控或杀掉它 |
| nohup | "no hangup（不挂断）" | 让命令不受挂断信号影响地运行，所以关终端也不会杀掉它 |
| SSH | "连服务器" | Secure Shell，一种加密协议，用来在远程机器上跑命令 |

---

[English（英文原文）](../../../../../phases/00-setup-and-tooling/10-terminal-and-shell/docs/en.md) · [示例代码](../../../../../phases/00-setup-and-tooling/10-terminal-and-shell/code) · [课后自测](../quiz.md) · [中文目录](../../../../README.md)
