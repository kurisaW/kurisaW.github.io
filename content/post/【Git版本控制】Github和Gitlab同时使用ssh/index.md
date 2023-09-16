---
title: 【Git版本控制】Github和Gitlab同时使用ssh
description: 最近在使用WSL时会同时用到GitHub和Gitlab，因此与传统配置ssh方式有些不一样的地方，这里特别记录一下
slug: 【Git版本控制】Github和Gitlab同时使用ssh
date: 2023-09-16 00:00:00+0000
image: cover.jpg
categories:
    - Git版本控制
tags:
    - Git
    - ssh
---



## 前言

最近在使用 WSL 时会同时用到 GitHub和 Gitlab ，因此与传统配置 ssh 方式有些不一样的地方，这里特别记录一下

## 本地生成公私密钥

首先确保把之前的 ssh 信息清除，也可以将整个 `~/.ssh` 目录删除

```bash
rm -rf ~/.ssh/*
```

我们分别生成 Github 和 Gitlab账号的 SSH 密钥

* Github 生成密钥

```bash
ssh-keygen -t rsa -C 2053731441@qq.com -f ~/.ssh/github_id-rsa
```

* Gitlab 生成密钥

```bash
ssh-keygen -t rsa -C wangyuqiang@rt-thread.com -f ~/.ssh/gitlab_id-rsa
```

注意不要选择其他操作，一路回车即可

此时打开 `~/.ssh/` 目录可以看到生成了四个文件：`github_id-rsa  github_id-rsa.pub  gitlab_id-rsa  gitlab_id-rsa.pub`

其中 `.pub` 后缀的文件为公钥，需要上传到远程仓库SSH；没有后缀的则是私钥，本地留存

## 远程仓库 SSH 填写公钥密钥

我们先打开 Github 的 Settings选项，然后选择 `SSH and GPG keys->New SSH key` ，`Title`可以随意拟定，`Key`需要查看刚刚的 `github_id-rsa.pub` 文件，并且复制到  Gitlab 的`key`一栏中；

Gitlab 的操作方式与 Github 类似，具体步骤：

打开 `Gitlab -> 用户设置 -> SSH密钥` ，在密钥一栏填入 `gitlab_id-rsa.pub`文件中的具体值，标题自拟即可。

## 配置不同 Host 的 SSH Key

回到 `~/.ssh/` 目录下，并且创建一个名为 `config` 的文件，在该文件中填写以下具体代码，其中部分参数依照自己的信息填写：

```bash
#github
Host github.com
    Hostname ssh.github.com
    Port 443
    User git
    IdentityFile ~/.ssh/github_id-rsa

#gitlab
host rt-thread.com
    Hostname git.rt-thread.com
    User git
    IdentityFile ~/.ssh/gitlab_id-rsa
```

![](.\figure\ssh-config.png)

## 验证

使用下面的命令分别验证 Github 和 Gitlab的 SSH 配置

* Github SSH 验证

```bash
ssh -T git@github.com
```

* Gitlab SSH 验证

```bash
ssh -T git@rt-thread.com
```

如果出现如下提示即表示远程仓库 SSH 公钥和本地 SSH 密钥配对成功

![](.\figure\valid-ssh.png)
