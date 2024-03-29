---
title: 【Matter】Nordic-Mattter开发大纲
description: 这部分仅作为开发大纲，后面会出一系列系统教程，以 Matter over Thread：在一台设备上配置边界路由器和控制器 为例。
slug: 【Matter】Nordic-Mattter开发大纲
date: 2023-06-07 00:00:00+0000
image: cover.jpg
categories:
    - Matter
tags:
    - Matter
    - Nordic
    - BLE 
---

## nRF Connect SDK 支持Mattter

* [Nordic提供的Matter用户指南](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/index.html)

> 子页面：
>
> - [Matter概况](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/overview/index.html)
> - [开始使用Matter](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/getting_started/index.html)
> - [如何创建 Matter 最终产品](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/end_product/index.html)

## Matter网络拓扑结构

![image-20230601200431602](https://cdn.jsdelivr.net/gh/kurisaW/picbed/img2023/202306012004778.png)

* `Thread`：Thread是一种开放的低功耗无线通信协议，旨在为物联网设备提供安全、稳定、高效的IPv6连接。它基于IEEE 802.15.4标准，支持多种应用场景，如智能家居、建筑自动化、工业自动化等。Thread协议的特点是易于扩展、安全性高、可靠性好、覆盖范围广、低功耗等。
* `WI-FI`：Wi-Fi是一种无线局域网技术，采用IEEE 802.11标准，可以实现高速的无线数据传输。它广泛应用于智能手机、平板电脑、笔记本电脑、智能家居、智能电视等设备中，可以通过无线方式连接互联网和其他设备。Wi-Fi的主要特点是速度快、覆盖范围广、使用方便等。
* `Ethernet（以太网）`：Ethernet（以太网）是一种有线局域网技术，采用IEEE 802.3标准，可以通过网线连接设备和网络。它是一种广泛应用于计算机网络中的技术，可以实现高速的数据传输和可靠的网络连接。Ethernet的主要特点是速度快、可靠性高、稳定性好等。
* `Matter binding（Matter协议）`：Matter是一个由智能家居设备制造商、芯片厂商和互联网巨头等多个公司发起的开放性联盟，旨在促进智能家居设备之间的互操作性和互连性。Matter协议是该联盟发布的一种通信协议，可以让智能家居设备之间相互通信和交互。Matter协议的特点是开放性强、互操作性好、安全性高、可扩展性强等。Matter binding是指将Matter协议与其他通信协议（如蓝牙、Wi-Fi等）进行绑定，实现智能家居设备之间的互连和互操作。

## 硬件平台

运行 Matter 协议应用程序的硬件必须满足规范要求，包括提供适量的闪存以及能够同时运行蓝牙 LE 和 Thread 或 Wi-Fi。

> [硬件参考](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/getting_started/hw_requirements.html)

- Nodic nRF52840
- PC: Ubuntu（20.04 或更新版本）
- Raspberry Pi 4（以及内存至少为 8 GB 的 SD 卡）
- 支持 IPv6 的 Wi-Fi 接入点（路由器上未启用 IPv6 路由器广告防护）
- RF52840 DK 或 nRF52840 Dongle - 用于无线电协处理器 (RCP) 设备
- 兼容 Nordic Semiconductor 的 DK - 用于 Matter 附件设备（与其中一个[Matter 样本](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/samples/matter.html#matter-samples)兼容并编程）

## 软件平台

Linux PC withsoftware installed:


* [nRFConnectSDK v2.1.1](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/2.1.1/nrf/getting_started.html)

* [nRFCommand-line tools](https://www.nordicsemi.com/Products/Development-tools/nrf-command-line-tools/download)

* [Visual Studio Code withnRFConnect ExtensionPack for VS Code ](https://nrfconnect.github.io/vscode-nrf-connect/)

* [RaspberryPi 4 runningOpenThreadBorder Router](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/ug_thread_tools.html#installing-otbr-manually-raspberry-pi)

## 商业Matter生态系统测试方式

对于matter设备在不同协议下的配置和使用，官方提供以下几种方式：

- [Matter over Thread：在不同的设备上配置边界路由器和 Linux/macOS 控制器](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/getting_started/testing/thread_separate_otbr_linux_macos.html)
- [Matter over Thread：在一台设备上配置边界路由器和控制器](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/getting_started/testing/thread_one_otbr.html)
- [Matter over Wi-Fi：为 Linux 或 macOS 配置 CHIP 工具](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/getting_started/testing/wifi_pc.html)

**注意：这里我们基于[Matter over Thread：在一台设备上配置边界路由器和控制器](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/getting_started/testing/thread_one_otbr.html)进行过程演示。**

---

## Matter over Thread：：在一台设备上配置边界路由器和控制器

如果你只有一台设备，无论是装有 Linux 的 PC 还是 Raspberry Pi，你都可以设置和测试 Matter over Thread 开发环境，同时在这台设备上运行 Thread Border Router 和 Matter 控制器。

在此设置中，PC 或 Raspberry Pi 同时运行 Thread Border Router 和适用于 Linux 或 macOS 的 CHIP 工具。为了简化 Thread 与 Matter 附件设备的通信，使用带有 OpenThread Border Router 图像的 Docker 容器，而不是本地安装 OpenThread Border Router。

下面是在同一台设备上设置 OpenThread Board Router 和 Matter 控制器的拓扑结构图，我们结合 CHIP TOOL 进行开发

![image-20230605205336833](https://cdn.jsdelivr.net/gh/kurisaW/picbed/img2023/202306052053960.png)



### 1.要求

若要使用此设置，需要以下硬件：

- 以下任意之一：
  - 1 台装有 Ubuntu 的电脑（20.04 或更高版本）
  - 1x Raspberry Pi Model 3B+ 或更高版本，配备 Ubuntu（20.04 或更高版本）而不是 Raspbian OS
- 1x 蓝牙 LE 加密狗（可以嵌入 PC 内部，就像在树莓派上一样）
- 1x nRF52840 DK 或 nRF52840 加密狗 - 用于无线电协处理器 （RCP） 设备
- 1x nRF52840 DK 或 nRF5340 DK - 用于物质附件设备（使用[物质样品](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/samples/matter.html#matter-samples)之一进行编程）)

### 2.配置环境

要在同一设备上配置和使用线程边界路由器和 Matter 控制器，请完成以下步骤。

#### Step1.对样品编程

使用可用的 [Matter 样本](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/samples/matter.html#matter-samples)之一对 Matter 附件设备的开发套件进行编程。 我们建议使用[Matter light bulb](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/samples/matter/light_bulb/README.html#matter-light-bulb-sample)。

#### Step2.Thread Border Router配置

在 PC 或树莓派上配置线程边界路由器，具体取决于您使用的硬件。 有关详细步骤，请参阅 nRF Connect SDK 文档中 [Thread Border Router](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/thread/tools.html#ug-thread-tools-tbr)页面上的使用 Docker 运行 OTBR 部分。

#### Step3.Chip Tool配置

适用于 Linux 或 macOS 的 CHIP Tool 是 [Matter controller](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/overview/network_topologies.html#ug-matter-configuring-controller) 角色的默认实现，建议用于 nRF Connect 平台。 对于此线程问题，您将在与线程边界路由器相同的设备上配置控制器。

完成以下步骤：

a. 选择以下选项之一：

   - 仅适用于 Linux - 使用 [Matter nRF Connect 发布](https://github.com/nrfconnect/sdk-connectedhomeip/releases) GitHub 页面中的预构建工具包。 确保程序包与 nRF Connect SDK 版本兼容。
   - 对于 Linux 和 macOS - 从目录中可用的源文件手动构建它，并使用 Matter 文档中使用 [CHIP TOOL](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/matter/chip_tool_guide.html)页面中的构建说明。`modules/lib/matter/examples/chip-tool`

b. 配置芯片工具控制器。 按照 Matter 文档中的使用 [CHIP TOOL](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/matter/chip_tool_guide.html)用户指南中的步骤完成以下操作：

   - 通过完成“构建和运行 CHIP 工具”中列出的步骤来构建和运行 CHIP TOOL。
   - 通过完成“使用 CHIP 工具进行物质设备测试”中列出的步骤来准备测试环境。

#### Step4.例程测试

根据您在开发工具包上编程的 Matter 示例，转到对应示例的文档页面并完成“测试”部分中的步骤。

## 结语

这部分仅作为开发大纲，后面会出一系列系统教程，以**Matter over Thread：：在一台设备上配置边界路由器和控制器**为例。

---

* [Nordic-Matter 演示教学](https://www.youtube.com/watch?v=9Ar13rMxGIk&t=554s)

* [Matter over Thread: Configuring Border Router and controller on one device](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/protocols/matter/getting_started/testing/thread_one_otbr.html)
