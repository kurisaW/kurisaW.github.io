---
title: 【Linux系统开发】Linux常见问题汇总
description: 汇总一些常用的Linux问题解决方案（持续更新中...）
slug: 【Linux系统开发】Linux常见问题汇总
date: 2023-10-09 00:00:00+0000
image: cover.jpg
categories:
    - Linux
tags:
    - ubuntu
    - Linux
---



## 1.vmware tools 灰色无法点击

执行如下步骤：

```bash
sudo apt-get update

sudo apt-get upgrade

sudo apt-get install open-vm-tools-desktop -y
```

## 2.linux安装搜狗输入法

终端安装 fcitx

```bash
sudo apt-get install fcitx
```

到搜狗官方下载 deb 包：

> * https://shurufa.sogou.com/linux

使用linux自带的安装程序安装输入法后，安装如下输入法依赖：

```bash
sudo apt install libqt5qml5 libqt5quick5 libqt5quickwidgets5 qml-module-qtquick2
sudo apt install libgsettings-qt1
```

重启即可

