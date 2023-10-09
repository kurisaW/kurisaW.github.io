---
title: 【Git版本控制】在Linux终端显示Git版本信息
description: 如何在Git中显示当前分支
slug: 【Git版本控制】在Linux终端显示Git版本信息
date: 2023-10-09 00:00:00+0000
image: cover.jpg
categories:
    - Git版本控制
tags:
    - Git
    - CI
    - scripy
---



## 前言

在使用Git管理项目时，经常需要知道当前所在的分支是哪一个。这个信息对于协作和版本控制非常重要。然而，Git默认情况下并不会在命令行中显示当前分支名称，这可能会导致一些混淆和不便。在本篇博文中，我们将介绍如何通过编辑`.bashrc`文件，使Git在命令行中显示当前分支的名称，让你的Git工作更加顺畅和高效。

### 步骤一：进入home目录

首先，打开你的终端，并进入home目录。你可以使用以下命令来完成这一步：

```shell
cd ~
```

### 步骤二：编辑.bashrc文件

接下来，我们需要编辑`.bashrc`文件，这是Linux和macOS系统中存储Shell配置的文件。你可以使用vi编辑器或其他文本编辑器来打开它，这里我们以vi为例：

```shell
vi .bashrc
```

### 步骤三：添加代码到文件末尾

在打开的`.bashrc`文件中，将以下代码添加到文件的末尾：

```shell
function git_branch {  
   branch="`git branch 2>/dev/null | grep "^\*" | sed -e "s/^\*\ //"`"  
   if [ "${branch}" != "" ];then  
       if [ "${branch}" = "(no branch)" ];then  
           branch="(`git rev-parse --short HEAD`...)"  
       fi  
       echo " ($branch)"  
   fi  
}  

export PS1='\u@\h \[\033[01;36m\]\W\[\033[01;32m\]$(git_branch)\[\033[00m\] \$ '
```

这段代码定义了一个名为`git_branch`的函数，用于获取并显示当前Git分支的名称。然后，通过`export`命令将这个信息添加到Shell的提示符中，以便在命令行中实时显示当前分支名称。

### 步骤四：保存并退出vi编辑器

完成以上代码的添加后，按下Esc键退出编辑模式，然后输入以下命令保存并退出vi编辑器：

```
:wq
```

### 步骤五：执行命令使配置生效

最后，执行以下命令来使新的配置生效：

```shell
source ./.bashrc
```

现在，当你进入一个包含Git仓库的目录时，命令行提示符将会显示当前分支的名称，让你随时了解项目的状态。

通过这个简单的配置，你可以提高Git工作的效率，更轻松地进行版本控制和协作。希望这个小技巧对你的开发工作有所帮助！
