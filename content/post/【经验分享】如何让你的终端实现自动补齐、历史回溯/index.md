---
title: 【经验分享】如何让你的终端实现自动补齐、历史回溯
description: 如何让你的终端实现自动补齐、历史回溯等功能，提升你的开发效率
slug: 【经验分享】如何让你的终端实现自动补齐、历史回溯
date: 2024-02-03 15:00:00+0000
image: cover.jpg
categories:
    - experience_sharing
tags:
    - experience sharing
---


## Linux下配置

在 Linux 系统上配置 oh-my-zsh 并更改主题以及启用历史回溯非常简单。下面是详细步骤：

### 步骤 1: 安装 zsh

确保你的系统上已经安装了 zsh。你可以使用系统的包管理器进行安装。例如，在基于 Debian/Ubuntu 的系统上，你可以运行：

```bash
sudo apt-get install zsh
```

### 步骤 2: 安装 oh-my-zsh

在终端中运行以下命令来安装 oh-my-zsh：

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

或者，如果你没有安装 `curl`，可以使用 `wget`：

```bash
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

### 步骤 3: 更改主题

1. 打开 `~/.zshrc` 文件以编辑它：

    ```bash
    nano ~/.zshrc
    ```

2. 找到 `ZSH_THEME` 行并更改主题。你可以在 [oh-my-zsh 主题库](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)中选择一个主题，例如：

    ```bash
    ZSH_THEME="agnoster"
    ```

3. 保存并关闭文件。

### 步骤 4: 启用历史回溯

oh-my-zsh 默认启用历史回溯。确保 `~/.zshrc` 中没有明确禁用该功能的设置。检查是否存在以下行：

```bash
HIST_STAMPS="yyyy-mm-dd"
```

这将显示历史命令的时间戳。如果你想要简单地显示命令历史而不包含时间戳，可以将其设置为：

```bash
HIST_STAMPS=""
```

### 步骤 5: 重新启动 zsh 或打开新终端

在更改 `~/.zshrc` 文件后，你需要重新启动 zsh 或者打开一个新的终端窗口以应用更改。

```bash
source ~/.zshrc
```

现在，你的 oh-my-zsh 应该已经配置好，并且你可以享受新的主题和命令历史回溯功能。如果你在终端中输入 `zsh` 并按 Enter，也可以切换到 zsh 提示符，体验更改后的主题和配置。

## Windwos下配置

在 Windows 下，你可以使用一些工具来实现类似 oh-my-zsh 的命令历史显示和补全功能。其中之一是使用 PowerShell，并安装 `PSReadLine` 模块，它提供了丰富的命令行编辑和历史记录功能。

以下是在 PowerShell 中配置类似 oh-my-zsh 的历史记录显示的步骤：

1. **安装 PSReadLine 模块:**
   打开 PowerShell 终端，并执行以下命令来安装 `PSReadLine` 模块：
   ```powershell
   Install-Module -Name PSReadLine -Force -SkipPublisherCheck
   ```

2. **配置 PowerShell 用户配置文件:**
   执行以下命令打开 PowerShell 配置文件（如果不存在，会创建一个新文件）：
   ```powershell
   notepad $PROFILE
   ```

3. **在配置文件中添加以下行:**
   在打开的配置文件中，添加以下内容：
   ```powershell
   Import-Module PSReadLine
   
   Set-PSReadLineOption -HistoryNoDuplicates:$false
   Set-PSReadLineOption -EditMode Emacs
   ```

   保存并关闭文件。

4. **重新启动 PowerShell:**
   关闭当前的 PowerShell 终端，并重新打开一个新的终端。

5. **使用历史记录搜索:**
   可以在 PowerShell 终端中使用 `Ctrl + r` 来搜索并显示命令历史记录。输入字符，它会匹配历史记录中的命令。
