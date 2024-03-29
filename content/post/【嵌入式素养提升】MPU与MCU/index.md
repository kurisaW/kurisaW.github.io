---
title: 【嵌入式素养提升】MPU与MCU
description: 计算、控制单元小型化后出现的技术，集成电路进步带来的计算机系统集成程度提高的结果。
slug: 【嵌入式素养提升】MPU与MCU
date: 2023-11-04 00:00:00+0000
image: cover.jpg
categories:
    - 嵌入式素养提升
tags:
    - MCU
    - MPU

---



## MPU与MCU

MPU全名称为 Micro processor Unit，MCU全称为Micro Controller Uint，首先这两个词都带有一个Micro开头，这就表明了这是计算、控制单元小型化后出现的技术，由于集成电路进步带来的计算机系统集成程度提高的结果，是的原来有多片分化的组成的计算机系统向高度集成化发展，多个芯片或元件的功能在向一颗芯片集中，这也是一个大的技术演进的背景。

但是在这种技术的演进过程中，出现了两种不同的需求：“以软制硬”和“以硬助软”。所谓以软制硬，就是通过一段软件程序来控制硬件，也就是所谓的“程控”，在这种使用模式下，计算机系统不承担主要的工作负载，而主要起辅助、协调、控制作用。

在这种情况下集成化的计算机系统就不需要太强大的计算、处理能力，所以对应的形态应该是运行频率低、运算能力一般，但是需要集成化的程度高（使用方便）、价格低廉（辅助系统不应该增加太多成本）等因素。

由于主要完成“控制”相关的任务，所以称为 `Controller`。也就是根据外界信号（刺激），产生一些响应，做点简单的人机界面。对于这种需求，通常不需要芯片主频太高。在早期的8051系列主频不过是10几MHZ，还是12个周期执行一条指令。而经过多年的“魔改”，最终也达到了100MHZ。其次就是处理能力不强，8位的MCU长期是微控制器的主流，而后来16位的MCU逐步开始占领市场，随着ARM的32位MCU的出现，采用ARM的M系列MCU也开始逐步扩大市场，并以ST、NXP公司的产品为主要代表。但是这些ARM的M系列MCU的主频一般也是在几十MHZ和100多MHZ的量级。再然后由于执行的“控制相关”的任务，通常不需要支持负载的图形界面和处理能力。在MCU上完成的任务大多数情况下是一些简单的刺激-响应式的任务，而且任务类型单一，任务执行过程简单。在这种情况下一般不需要MCU去执行功能复杂、运算量大的程序，因此通过也不需要运行大型操作系统来支持复杂的多任务管理，这就造成了MCU一般对于存储器的容量要求比较低。

而`Processor`，顾名思义就是处理器。处理器就是能够执行“处理”功能的器件，其实具备Processor 这个单词的器件不少，比如CPU就成为“中央处理器”，那既然有“中央”就应该有“外围”。GPU在经典的桌面计算机中就是一个典型的“外围”设备，主要负责图形图像处理。

以上对处理器说了这么多，核心意思就是一个，处理器一定要处理/运算能力强，能够执行比较复杂的任务；而微处理器，其实就是微型化/集成化了的处理器，标准来说是微型化/集成化的“中央处理器”，这就是把传统的CPU之外继承了原属于“芯片组”的各类接口和部分“外设”而形成的。MPU从一开始就定位了具备相当的处理和运算能力，一般需要运行较大的操作系统来实现复杂的任务处理。因此这就决定了MPU应该具备比较高的主频和较为强大的运算能力。

为了支撑MPU强大的算力，是的“物尽其用”，必然要求在MPU上运行比较复杂的、运算量大的程序和任务，通常需要有大容量的存储器来配合支撑。而大容量的存储器难以被集成到以逻辑功能为主的MPU内部，因此通常需要“外挂”大容量的存储器，主要是大容量的DDR存储器和FLASH，在手机领域，前者被称为“运存”，而后者被称之为“内存”，为了支撑运行复杂操作系统和大型程序，往往还需要MPU中集成高性能的存储控制器、存储管理单元（MMU）等一套复杂的存储机制和硬件。

从形态上看，MPU由于需要运行对处理能力要求复杂的大程序，一般都需要外挂存储器才能运行起来。而MCU往往只是执行刺激-响应式的过程控制和辅助，功能比较单一，仅仅需要使用偏上集成的小存储器即可。这是区分MPU和MCU的重要表象，但不是核心原因。

总结一下，MPU和MCU的区别本质上是因为应用定位的不同，为了满足不同的应用场景而按不同方式优化出来的两类器件。MPU注重通过较为强大的运算/处理能力，执行复杂多样的大型程序，通常需要外挂大容量的存储器。而MCU通常运行比较单一的任务，执行对于硬件设备的管理/控制功能，通常不需要很强的运算/处理能力，因此也不需要有大容量的存储器来支撑运行大程序，通常以单片机集成的方式在单个芯片内部集成小容量的存储器实现系统的“单片化”。

