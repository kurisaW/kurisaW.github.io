---
title: 【Matter】CHIP设备层设计笔记
description: 本文档包含与 CHIP 设备层 ( `src/platform`) 内部设计相关的概述、注释和其他信息材料。它旨在作为对实现者有价值的主题的托管文档的地方。
slug: 【Matter】CHIP设备层设计笔记
date: 2023-08-20 00:00:00+0000
image: cover.jpg
categories:
    - Matter
tags:
    - Matter
    - Platform
---

# CHIP设备层设计笔记

本文档包含与 CHIP 设备层 ( `src/platform`) 内部设计相关的概述、注释和其他信息材料。它旨在作为对实现者有价值的主题的托管文档的地方，但由于大小或范围的原因，它自然不适合代码中的注释。

这是一个动态文档，具有非正式的结构，随代码一起发展。我们鼓励开发人员添加他们认为对其他工程师有用的东西。

本文档包含以下部分：

- [设备层适配模式](https://github.com/project-chip/connectedhomeip/tree/master/src/platform#Device-Layer-Adaptation-Patterns)

------

### 设备层适配模式

设备层使用各种设计模式，使代码更容易适应不同的平台和操作环境。

CHIP 设备层旨在跨各种平台和操作环境工作。这些环境可能因系统类型、操作系统、网络堆栈和/或线程模型而异。设备层的目标之一是使 CHIP 应用程序堆栈能够轻松适应新环境。在新平台与现有改编基本相似的情况下，这是特别理想的。

作为其设计的一部分，CHIP 设备层支持代码重用模式，努力减少对预处理器条件（例如#ifdef）的需求。虽然没有完全消除#ifdef，但该设计允许将行为中的主要差异表示为不同的代码库（通常是单独的 C++ 类），然后通过组合将它们组合在一起以实现特定的适应。

为了提高应用程序的可移植性，CHIP 设备层采用静态多态性模式将其应用程序可见的 API 与底层特定于平台的实现隔离开来。设备层本身使用类似的接口模式来提供组件之间的划分。

尽可能通过使用零成本抽象模式（代码大小和执行开销方面的零成本）来实现上述目标。我们努力使模式易于使用，没有太多的概念负担或繁琐的语法。

以下各节描述了用于实现这些目标的一些模式。

1. [接口和实现类](https://github.com/project-chip/connectedhomeip/tree/master/src/platform#Interface-and-Implementation-Classes)
2. [方法转发](https://github.com/project-chip/connectedhomeip/tree/master/src/platform#Method-Forwarding)
3. [目标平台选择](https://github.com/project-chip/connectedhomeip/tree/master/src/platform#Target-Platform-Selection)
4. [通用实现类](https://github.com/project-chip/connectedhomeip/tree/master/src/platform#Generic-Implementation-Classes)
5. [覆盖通用行为](https://github.com/project-chip/connectedhomeip/tree/master/src/platform#Overriding-Generic-Behaviors)
6. [通用实现的多重继承和子类化](https://github.com/project-chip/connectedhomeip/tree/master/src/platform#Multiple-Inheritance-and-Subclassing-of-Generic-Implementations)
7. [通用实现行为的静态虚拟化](https://github.com/project-chip/connectedhomeip/tree/master/src/platform#Static-Virtualization-of-Generic-Implementation-Behavior)
8. [.cpp 文件和显式模板实例化](https://github.com/project-chip/connectedhomeip/tree/master/src/platform#-ipp-files-and-explicit-template-instantiation)

------

### 接口和实现类

CHIP设备层使用双类模式将组件对象的抽象特征（通常是其外部可见的方法）与特定平台上这些特征的具体实现分开。遵循这种模式，设备层中的每个主要组件都体现在（至少）两个 C++ 类中：一个抽象接口类和一个实现类。

外部可见的***抽象接口类***定义了一组通用方法（以及可能的其他成员），这些方法对组件用户普遍可用，但独立于底层实现。接口类本身不包含任何功能，而是使用零成本抽象技术将所有方法调用转发到关联的实现类。接口类用于形式化组件的功能接口，并提供托管与实现无关的 API 文档的位置。

实现***类***提供了接口类公开的逻辑功能的具体的、特定于平台的实现。这一功能可以由类本身直接提供（即在其方法内），或者通过委托给一个或多个辅助类来提供。

设备层的每个主要应用程序可见组件都存在成对的抽象接口类和实现类。此外，在设备层中定义了类似的类对，以帮助组件之间的隔离。

抽象接口类根据它们提供的功能来命名，例如ConfigurationManager、ConnectivityManager 等。实现类采用其接口类的名称并附加后缀`Impl`。在所有情况下，实现类都需要从其接口类公开继承。

```
class ConfigurationManagerImpl;

/** Interface class for ConfigurationManager component
 */
class ConfigurationManager
{
    using ImplClass = ConfigurationManagerImpl;

public:
    CHIP_ERROR GetDeviceId(uint64_t & deviceId);
    static CHIP_ERROR Init();
    ...
};

/** Concrete implementation of ConfigurationManager component for a specific platform
 */
class ConfigurationManagerImpl final
    : public ConfigurationManager
{
    ...
};
```

### 方法转发

接口类通过称为转发方法的短内联函数将***方法调用转发\***到其实现类。`this`这些方法通过向下转换对象的指针并调用实现类上类似命名的方法来转发来自应用程序的调用。此模式类似于 C++ [奇怪的重复模板模式](https://en.wikipedia.org/wiki/Curiously_recurring_template_pattern) ，不同之处在于基类和子类之间的关系是固定的，而不是表示为模板参数。接口内使用了类型别名named，`ImplClass`使转发方法定义更加简洁。

```
inline CHIP_ERROR ConfigurationManager::GetDeviceId(uint64_t & deviceId)
{
    /* forward method call... */
    return static_cast<ImplClass*>(this)->_GetDeviceId(deviceId);
}
```

该模式的一个便利功能是它允许转发静态方法以及实例方法。例如：

```
inline CHIP_ERROR ConfigurationManager::Init()
{
    return ImplClass::_Init();
}
```

作为转发方法目标的实现类上的方法称为***实现方法\***。每一种转发方法都必须有相应的实现方法。

前导下划线（_）用于区分实现方法与其转发方法。这种安排有助于强调两者之间的区别，并确保在实现者忽略提供实现方法时生成编译错误。

实现方法并不意味着直接调用。为了阻止这种类型的使用，实现类将其实现方法声明为私有，然后使用友元声明为接口类提供（唯一）调用这些方法作为转发的一部分的权利。

```
class ConfigurationManagerImpl;

/** Interface class for ConfigurationManager component
 */
class ConfigurationManager
{
    using ImplClass = ConfigurationManagerImpl;

public:
    CHIP_ERROR GetDeviceId(uint64_t & deviceId);
    static CHIP_ERROR Init();
    ...
};

/** Concrete implementation of ConfigurationManager component for specific platform
 */
class ConfigurationManagerImpl final : public ConfigurationManager
{
    /* Let the forwarding methods on ConfigurationManager call implementation
       methods on this class. */
    friend ConfigurationManager;

private:
    CHIP_ERROR _GetDeviceId(uint64_t & deviceId);
    static CHIP_ERROR _Init();
    ...
};

inline CHIP_ERROR ConfigurationManager::GetDeviceId(uint64_t & deviceId)
{
    /* Forward calls to corresponding implementation method... */
    return static_cast<ImplClass*>(this)->_GetDeviceId(deviceId);
}

inline CHIP_ERROR ConfigurationManager::Init()
{
    /* Forward calls to corresponding static implementation method... */
    return ImplClass::_Init();
}
```

### 目标平台选择

实现类提供了在特定平台上使用的设备层组件的具体实现。同一组件的设备层源代码树中可能存在多个实现类。每个类都具有相同的名称，但它们的代码对于相关平台来说是唯一的。在编译时选择包含哪个实现类是通过计算的 #include 指令完成的，其形式如下：

```
/* contents of ConfigurationManager.h */

...

#define CONFIGURATIONMANAGERIMPL_HEADER \
        <platform/CHIP_DEVICE_LAYER_TARGET/ConfigurationManagerImpl.h>
#include CONFIGURATIONMANAGERIMPL_HEADER

...
```

该指令出现在定义组件接口类的头文件中。C++ 预处理器自动扩展 #include 行以根据所选平台选择适当的实现标头。这样，包含组件接口头文件的源文件自然也可以获得正确的实现头文件。

每个受支持平台的实现头文件都排列在以其目标平台命名的子目录中（例如`ESP32`）。所有此类文件都具有相同的文件名（例如`ConfigurationManagerImpl.h`），并且每个文件都包含类似名称的类的定义（`ConfigurationManagerImpl`）。

特定于平台的源文件放置在紧邻设备层根源目录下面的子目录中（例如 `src/adaptations/device-layer/ESP32`）。与特定于平台的头目录一样，这些子目录以目标平台命名。

设备层目标平台的选择是在项目配置时使用配置脚本选项指定的 `--device-layer=<target-platform>`。传递 --device-layer 选项会导致一对预处理器符号的定义，其中目标平台的名称已合并到定义中。例如：

```
#define CHIP_DEVICE_LAYER_TARGET ESP32
#define CHIP_DEVICE_LAYER_TARGET_ESP32 1
```

--device-layer 配置选项还选择要包含在生成的库文件中的适当的特定于平台的源文件集。这是通过设备层 Makefile.am 中的逻辑完成的。

### 通用实现类

通常可以在一系列平台上共享实现代码。在某些情况下，所有目标的相关代码基本上都是相同的，每种情况下只需要进行少量的定制。在其他情况下，实现的通用性扩展到共享特定架构功能的平台子集，例如通用操作系统（Linux、FreeRTOS）或网络堆栈（套接字、LwIP）。

为了适应这一点，CHIP 设备层鼓励采用一种将通用功能分解为***通用实现基类的\***模式。然后，这些基类用于组成（通过继承）构成组件基础的具体实现类。

通用实现基类被实现为遵循 C++ [奇怪重复模板模式的](https://en.wikipedia.org/wiki/Curiously_recurring_template_pattern)C++ 类模板。希望合并常见行为的实现类从模板的实例继承，将实现类本身作为模板的参数传递。

```
/** Generic base class for use in implementing ConfigurationManager components
 */
template<class ImplClass>
class GenericConfigurationManagerImpl
{
    ...
};

/** Concrete implementation of ConfigurationManager component for specific platform
 */
class ConfigurationManagerImpl final
    : public ConfigurationManager,
      public GenericConfigurationManagerImpl<ConfigurationManagerImpl> /* <-- Implementation provided by
                                                                              generic base class. */
{
    ...
};
```

在许多情况下，通用实现基类本身将直接提供满足组件接口所需的部分或全部实现方法。C++ 方法解析的规则是对接口类上的转发方法的调用直接映射到基类方法。在这种情况下，派生实现类根本不需要声明目标方法的版本，并且方法调用在编译时静态转发，没有任何开销。

```
/** Interface class for ConfigurationManager component
 */
class ConfigurationManager
{
    using ImplClass = ConfigurationManagerImpl;

public:
    CHIP_ERROR GetDeviceId(uint64_t & deviceId);
    static CHIP_ERROR Init();
    ...
};

/** Generic base class for use in implementing ConfigurationManager components
 */
template<class ImplClass>
class GenericConfigurationManagerImpl
{
protected:
    CHIP_ERROR _GetDeviceId(uint64_t & deviceId); /* <-- Invoked when GetDeviceId() called. */
    ...
};

/** Concrete implementation of ConfigurationManager component for specific platform
 */
class ConfigurationManagerImpl final
    : public ConfigurationManager,
      public GenericConfigurationManagerImpl<ConfigurationManagerImpl>
{
    ...
};
```

### 覆盖通用行为

如果需要，具体实现类可以自由地覆盖通用基类提供的实现方法。这是通过在实现类上定义该方法的特定于平台的版本来完成的。C++ 的规则导致优先于泛型方法调用实现类上的方法。

新方法可以完全取代通用方法的行为，或者可以通过在其自己的实现过程中调用通用方法来增强其行为。

```
CHIP_ERROR ConfigurationManagerImpl::_GetDeviceId(uint64_t & deviceId)
{
    using GenericImpl = GenericConfigurationManagerImpl<ConfigurationManagerImpl>;

    /* Call the generic implementation to get the device id. */
    uint64_t deviceId = GenericImpl::_GetDeviceId(deviceId);

    /* Special case the situation where the device id is not known. */
    if (deviceId == kNodeIdNotSpecified) {
        deviceId = PLATFORM_DEFAULT_DEVICE_ID;
    }

    return deviceId;
}
```

### 通用实现的多重继承和子类化

具体实现类可以自由地从多个通用基类继承。当组件的整体功能可以自然地分割成独立的片（例如支持 WiFi 的方法和支持 Thread 的方法）时，此模式特别有用。然后，每个这样的切片都可以通过一个不同的基类来实现，该基类最终在最终实现中与其他基类组合在一起。

```
/** Concrete implementation of ConfigurationManager component for specific platform
 */
class ConfigurationManagerImpl final
    : public ConfigurationManager,
      public GenericWiFiConfigurationManagerImpl<ConfigurationManagerImpl>, /* <-- WiFi features */
      public GenericThreadConfigurationManagerImpl<ConfigurationManagerImpl> /* <-- Thread features */
{
    ...
};
```

通用实现基类还可以从其他通用基类继承。这对于“专门化”特定用例子范围（例如，特定操作系统类型）的通用实现非常有用。

```
/** Generic base class for use in implementing PlatformManager features
 *  on all platforms.
 */
template<class ImplClass>
class GenericPlatformManagerImpl
{
    ...
};

/** Generic base class for use in implementing PlatformManager features
 *  on FreeRTOS platforms.
 */
template<class ImplClass>
class GenericPlatformManagerImpl_FreeRTOS
    : public GenericPlatformManagerImpl<ImplClass>
{
    ...
};
```

### 通用实现行为的静态虚拟化

在创建通用实现基类时，如果操作可能或必须以特定于平台的方式实现，则鼓励开发人员使用静态虚拟化模式将操作委托给具体实现类。

例如，考虑 ConfigurationManager 组件的通用实现，其中值访问器方法通过`GetDeviceId()`从底层键值存储中检索值来进行操作。键值存储的实现方式的细节可能会因平台而异。为了实现这一点，通用实现类被构造为将检索键值的操作委托给具体实现类上的方法。

`this`遵循奇怪的重复模板模式，通过将指针强制转换为实现类并调用具有适当签名的方法来完成委托。名为 的内联辅助函数`Impl()`有助于使代码简洁。

```
template<class ImplClass>
class GenericConfigurationManagerImpl
{
protected:
    CHIP_ERROR _GetDeviceId(uint64_t & deviceId);
    ...
private:
    ImplClass * Impl() { return static_cast<ImplClass*>(this); }
};

class ConfigurationManagerImpl final
    : public ConfigurationManager,
      public GenericConfigurationManagerImpl<ConfigurationManagerImpl>
{
    friend GenericConfigurationManagerImpl<ConfigurationManagerImpl>;
private:
    CHIP_ERROR ReadConfigValue(const char * key, uint64_t & value);
};

template<class ImplClass>
CHIP_ERROR GenericConfigurationManagerImpl<ImplClass>::_GetDeviceId(uint64_t & deviceId)
{
    /* delegate to the implementation class to read the 'device-id' config value */
    return Impl()->ReadConfigValue(“device-id”, deviceId);
}

CHIP_ERROR ConfigurationManagerImpl::ReadConfigValue(const char * key, uint64_t & value)
{
    /* read value from platform-specific key-value store */
    ...
}
```

在上面的示例中，委托方法在概念上是“纯虚拟”的，因为具体实现类必须提供该方法的版本，否则编译将失败。在其他情况下，可以使用类似的模式来允许实现根据需要覆盖基类提供的默认行为。

同样，委托是通过转换`this`指针并调用适当的方法来发生的。然而，在这种情况下，通用基类提供了目标方法的默认实现，除非子类重写它，否则将使用该目标方法。

```
template<class ImplClass>
class GenericPlatformManagerImpl
{
protected:
    void _DispatchEvent(const CHIPDeviceEvent * event);
    void DispatchEventToApplication(const CHIPDeviceEvent * event);
    ...
private:
    ImplClass * Impl() { return static_cast<ImplClass*>(this); }
};

template<class ImplClass>
void GenericPlatformManagerImpl<ImplClass>::_DispatchEvent(const CHIPDeviceEvent * event)
{
    ...
    /* Delegate work to method that can be overridden by implementation class */
    Impl()->DispatchEventToApplication(event);
    ...
}

template<class ImplClass>
void GenericPlatformManagerImpl<ImplClass>::DispatchEventToApplication(const CHIPDeviceEvent * event)
{
    /* provide default implementation of DispatchEventToApplication() */
    ...
}
```

### .cpp 文件和显式模板实例化

C++ 模板的规则要求编译器在实例化时“查看”类模板的完整定义。（在此上下文中的实例化意味着编译器被迫根据模板提供的配方生成实际的类）。通常，这需要将类模板的整个定义（包括其所有方法）放入头文件中，然后必须在实例化之前将其包含在内。

为了将类模板的定义与其成员的定义分开，CHIP 设备层将所有非内联模板成员定义放入单独的文件中。该文件与模板头文件具有相同的基本名称，但带有后缀`.cpp`。这种模式减少了头文件中的混乱，并且可以仅在需要时才包含非内联成员定义（更多内容见下文）。

```
/* contents of GenericConfigurationManagerImpl.h */

template<class ImplClass>
class GenericConfigurationManagerImpl
{
protected:
    CHIP_ERROR _GetDeviceId(uint64_t & deviceId);
    ...
};
```

```
/* contents of GenericConfigurationManagerImpl.cpp */

template<class ImplClass>
CHIP_ERROR GenericConfigurationManagerImpl<ImplClass>::_GetDeviceId(uint64_t & deviceId)
{
    ...
}
```

通常情况下，C++ 编译器被迫多次实例化类模板，为其编译的每个 .cpp 文件实例化一次。这会显着增加编译过程的开销。[为了避免这种情况，设备层使用显式模板实例化](https://en.cppreference.com/w/cpp/language/class_template#Explicit_instantiation)的 C++11 技术 来指示编译器仅实例化模板一次。这是通过两个步骤完成的：首先，所有使用类模板的头文件`extern template class`在使用模板类之前都包含一个声明。这告诉编译器*不要*在该上下文中实例化模板。

```
/* contents of ConfigurationManagerImpl.h */

#include <CHIP/DeviceLayer/internal/GenericConfigurationManagerImpl.h>

// Instruct the compiler to instantiate the GenericConfigurationManagerImpl<ConfigurationManagerImpl>
// class only when explicitly asked to do so.
extern template class GenericConfigurationManagerImpl<ConfigurationManagerImpl>;

...
```

然后，在相应的 .cpp 文件中，包含模板的 .cpp 文件，并`template class`使用定义来强制显式实例化模板。

```
/* contents of ConfigurationManagerImpl.cpp */

#include <CHIP/DeviceLayer/internal/GenericConfigurationManagerImpl.cpp>

// Fully instantiate the GenericConfigurationManagerImpl<ConfigurationManagerImpl> class.
template class GenericConfigurationManagerImpl<ConfigurationManagerImpl>;

...
```

结果是，在编译引用的 .cpp 文件期间，模板的非内联成员仅被解析和实例化一次，从而避免了其他上下文中的冗余处理。
