---
title: 【Linux系统开发】Ubuntu配置SFTP服务
description: Linux多线程概念、inux线程实现、线程同步的方法、线程的互斥、互斥PK信号量、信号量操作、互斥操作、条件变量
slug: 【Linux系统开发】Ubuntu配置SFTP服务
date: 2023-04-07 00:00:00+0000
image: cover.jpg
categories:
    - Linux
tags:
    - SFTP
    - Linux
---

## SFTP介绍

SFTP是指Secure File Transfer Protocol，即安全文件传输协议。它提供了一种安全的网络加密方法来传输文件。SFTP与FTP具有几乎相同的语法和功能，是SSH的其中一部分，可安全地将文件传输到服务器。在SSH软件包中，已经包含了一个名为SFTP（Secure File Transfer Protocol）的安全文件信息传输子系统。SFTP本身没有单独的守护进程，必须使用sshd守护进程（默认端口号为22）来完成相应的连接和答复操作。因此，从某种意义上说，SFTP并不像服务器程序，而更像客户端程序。由于SFTP也使用加密传输认证信息和数据，因此使用SFTP非常安全。但是，由于这种传输方式使用了加密/解密技术，因此传输效率比普通的FTP要低得多。如果您对网络安全性要求更高，可以使用SFTP代替FTP。（参考资料：百度百科）

## 安装步骤

#### 1.目标：

在Ubuntu系统上开通SFTP文件服务，允许某些用户上传及下载文件。这些用户只能使用SFTP传输文件，不能使用SSH终端访问服务器，并且SFTP不能访问系统文件。系统管理员则既能使用SFTP传输文件，也能使用SSH远程管理服务器。
以下是将允许SFTP-users用户组内的用户使用SFTP，但不允许使用SSH Shell，且该组用户不能访问系统文件。在SFTP-users组内创建一个名为“SFTP”的用户。允许SSH-users用户组内的用户使用SFTP以及SSH。系统管理员的账户名为yifang。

#### 2.查看Ubuntu系统信息

![image-20230407101026858](https://raw.githubusercontent.com/kurisaW/picbed/main/img/202304071010234.png)

#### 3.检查是否已安装SFTP

在Linux系统中，一般RedHat系统默认已经安装了openssh-client和openssh-server，即默认已经集成了SFTP服务，不需要重新安装；而Ubuntu系统默认只安装了openssh-client，要用SFTP的话还需要安装openssh-server。如果系统已安装有openssh-client，则为了防止安装openssh-server时两者版本不兼容，可以先将openssh-client卸载后再安装。如下所示，如果Ubuntu没有安装SFTP，则会显示没有安装：

![image-20230407101132327](https://raw.githubusercontent.com/kurisaW/picbed/main/img/202304071011398.png)

```c
安装openssh-client: sudo apt-get install openssh-client
安装openssh-server: sudo apt-get install openssh-server
```

这里由于我已经完成安装了，此处就不做安装演示，具体下载命令如上所示。

#### 4.新建用户组SFTP-users，并新建用户SFTP

为了方便管理权限，创建用户组可以用于SFTP访问。然后创建sftp用户：

```c
sudo addgroup sftp-users
sudo adduser sftp (这部分会让你新建用户组信息，建议最好截图保存下)
```

#### 5.给SFTP赋权并新建用户组SSH-users

将SFTP从其他所有用户组中移除并加入SFTP-users组，然后关闭其Shell访问：

```c
sudo usermod -G sftp-users -s /bin/false sftp
```

创建SSH用户组，并将管理员添加到该组（请注意usermod命令中的-a参数意味着不从其他用户组中移除）。

```c
sudo addgroup ssh-users
sudo usermod -a -G ssh-users bbc2005
```

#### 6.创建并设置SFTP用户目录

为“监狱”根目录和共享目录做准备，“监狱”根目录必须满足以下要求：
所有者为root，其他任何用户都不能拥有写入权限。因此，为了让SFTP用户能够上传文件，还必须在“监狱”根目录下创建一个普通用户能够写入的共享文件目录。为了方便管理员通过SFTP管理上传的文件，把这个共享文件目录配置为由yifang所有，允许SFTP-users读写，这样，管理员和SFTP用户组成员都能读写这个目录。

```c
sudo mkdir /home/sftp_root
sudo mkdir /home/sftp_root/shared
sudo chown yifang:sftp-users /home/sftp_root/shared

sudo chmod 770 /home/sftp_root/shared
```

#### 7.修改SSH配置文件

在sshd\_config文件的最后添加以下内容：  

```c
vi /etc/ssh/sshd_config 
```

```c
AllowGroups ssh-users sftp-users  
Match Group sftp-users  
ChrootDirectory /home/sftp_root  
AllowTcpForwarding no  
X11Forwarding no  

ForceCommand internal-sftp
```

这些内容的意思是： 

* 只允许ssh-users和SFTP-users通过SSH访问系统；
* 针对SFTP-users用户，增加一些额外的设置：
  - 将/home/sftp_root设置为该组用户的系统根目录（因此它们将不能访问该目录之外的其他系统文件）；
  - 禁止TCP forwarding和X11 forwarding；强制该组用户只能使用SFTP。
  - 如果需要进一步了解细节，可以使用“man sshd_config”命令。这样设置之后，SSH用户组可以访问SSH，并且不受其他限制；而SFTP用户组仅能使用SFTP进行访问，并被限制在监狱目录中。

#### 8.SFTP客户端验证

首先将虚拟机重启：
```c
sudo reboot
```

在本地Windows系统中，可以通过SFTP客户端来连接Ubuntu系统的SFTP服务，例如使用RaiDrive。

查看ubuntu网络ip地址

```
ifconfig
```

![image-20230407103802472](https://raw.githubusercontent.com/kurisaW/picbed/main/img/202304071038531.png)zhe

这里我的IP地址为192.168.136.128。我们接着打开RaiDrive（安装配置可参考[RaiDrive—将网盘映射为磁盘](https://blog.devyi.com/archives/418/)）

![image-20230407104441660](https://raw.githubusercontent.com/kurisaW/picbed/main/img/202304071044734.png)

此时我们点击连接并连接成功后会自动在我们windows下自动生成一个名为SFTP的网络磁盘，这时候我们就可以在windows下对虚拟机进行文件操作了。

![image-20230407104643007](https://raw.githubusercontent.com/kurisaW/picbed/main/img/202304071046125.png)

