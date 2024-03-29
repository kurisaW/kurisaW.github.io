---
title: 【Linux系统开发】Linux常见开发汇总
description: 汇总一些常用的Linux问题解决方案（持续更新中...）
slug: 【Linux系统开发】Linux常见开发汇总
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

## 3.Cmake安装指定版本

首先去官网下载所需版本的压缩包：

> * https://cmake.org/files/

执行解压命令

```bash
tar -zxv -f cmake-3.22.6.tar.gz
```

安装相关依赖：

```bash
sudo apt-get install g++

sudo apt-get install libssl-dev

sudo apt-get install make
```

进入解压后的cmake文件，执行：

```
./bootstrap
```

编译构建：

```bash
make
```

安装：

```bash
sudo make install
```

## 4.ubuntu中使用 st-link

安装依赖项：

```bash
sudo apt-get install gcc build-essential cmake libusb-1.0 libusb-1.0-0-dev libgtk-3-dev pandoc
```

依次执行如下步骤：

```bash
# download source code
git clone https://github.com/stlink-org/stlink
cd stlink
# build
cmake .
make
# install
cd bin
sudo cp st-* /usr/local/bin
cd ../lib
sudo cp *.so* /lib32
# add rules
sudo cp stlink/config/udev/rules.d/49-stlinkv* /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo udevadm trigger
```

尝试烧录代码

```bash
#check if st-link is plugged
sudo st-info --probe

# write hex
sudo st-flash --format ihex write myapp.hex 

# 一般下载一次，会失败，需要刷入两次；
# write bin
sudo st-flash write in.bin 0x8000000 #stm32f4xx

# read bin
st-flash read out.bin 0x8000000 0x1000

# restart
# 向嵌入式控制器中下载一次，控制器就不运行了，需要重启一下，才能正常工作
sudo st-flash reset
```

具体的GDB调试可以参考这篇文章：

>   *   https://club.rt-thread.org/ask/article/cf31a215be3ee5e9.html
