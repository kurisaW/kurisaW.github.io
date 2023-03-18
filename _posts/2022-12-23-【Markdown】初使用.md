@[TOC]
# 目录
> 语法：@[TOC]
# 一级标题
## 二级标题
---
# 段落换行
## 解释
    段落的换行是两个以上的空格加回车
### 示例：
    *today is 2022/4/4*   

---
# 字体转换
## 1、*斜体文本*  
## 2、_斜体文本_
## 3、**粗体文本**
## 4、***粗斜体文本***
## 5、___粗斜体文本___
---
# 分隔线
## 1、***
## 2、___
## 3、---
---
# 文字删除线
## 解释
如果需要在文字上添加删除线，在文字两端分别加入两个波浪线（~~）即可
### 示例：   
    ~~当前文字废弃~~
---
# 文字下划线
## 解释
    在需要下划线的文本前面（< u >）

### 示例:
    注：<u>文本下划线</u>  注意：截取部分用< u >---< /u >
### <u>文字下划线</u>
---
# 脚注
##  格式： [^要注明的文本]
### 示例：创建脚注格式类似这样 [^RUNOOB]。
[^RUNOOB]: 菜鸟教程--学的不仅是技术，更是梦想！！
---
# Makedown列表
## 1.Makedown支持有序列表和无序列表
    使用星号（*）、加号（+）和减号（-）作为列表标记，这些标记后面需要加一个空格，再填写内容
### 示例：
#### (1)、无序列表
* ##### 第一项   
+ ##### 第二项
- ##### 第三项
#### (2)、有序列表
1. 第一项  
2. 第二项  
3. 第三项
## 2.列表嵌套
    列表嵌套只需要在子列表中的选项前面添加四个空格即可：
#### 示例：   
1. 列表一 
    * 第一个嵌套
    - 第二个嵌套   
2. 列表二  
    * 第一个嵌套  
    + 第二个嵌套
---
# Markdown区块
## 1.解释
Markdown 区块引用是在段落开头使用 > 符号 ，然后后面紧跟一个空格符号
### 示例：  
> 区块应用 
> 使用详情
## 2.区块嵌套
### 示例：
>区块应用
>>嵌套使用
>>>示例演示

>>次级嵌套  
>>>细节演示  
## 3.区块中列表使用  
### 示例：
>区块中使用列表
>>1. 第一项
>>+ 第一小项
>>+ 第二小项
>>2. 第二项
>>* 第一小项
>>- 第二小项
## 4.列表中使用区块
### 示例：
* 第一项
    > 第一小项 
    > 第二小项
* 第二项
---
# Markdown代码
## 解释
如果是段落上的一个函数或片段的代码可以用反引号把它包起来（`）
### 示例：  
`printf` 函数
## 代码区块
代码区块使用 4 个空格或者一个制表符（Tab 键）。
### 示例：
    #include<stdio.h>
    int main()
    {
        printf("Hello world!\n");
        return 0;
    }
你也可以用 ```包裹一段代码，并指定一种语言（也可以不指定）：
### 示例：
```javascript
$(document).ready(function () {
    alert('RUNOOB');
});
```
---
# Markdown链接  
使用方法如下：
>[链接名称]（链接地址）
或者
<链接地址>  

演示：
>[个人博客](https://blog.csdn.net/qq_56914146?type=blog)
or
<https://blog.csdn.net/qq_56914146?type=blog>
## 高级链接

我们可以通过变量来设置一个链接，变量赋值在文档末尾进行：
>这个链接用 1 作为网址变量 [Google][1]
这个链接用 runoob 作为网址变量 [blogs][blogs]
然后在文档的结尾为变量赋值（网址）

---
# Markdown图片

图片语法格式
>开头一个感叹号 !
接着一个方括号[]，里面放上图片的替代文字
接着一个普通括号()，里面放上图片的网址，最后还可以用引号包住并加上选择性的 'title' 属性的文字。

演示：![Yifang_Personalicon](https://img-blog.csdnimg.cn/img_convert/1508c35f1daec9ff3b7a8eb4a037a49b.png)
Markdown 还没有办法指定图片的高度与宽度，如果你需要的话，你可以使用普通的 <img> 标签。

>格式：\<img src="图片网址" width="缩放大小">
>
显示结果：
><img src="https://img-blog.csdnimg.cn/img_convert/1508c35f1daec9ff3b7a8eb4a037a49b.png" width="10%">

---
# Markdown表格
Markdown 制作表格使用 | 来分隔不同的单元格，使用 - 来分隔表头和其他行。

语法格式如下：
>|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |

演示结果：
|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |

**对齐方式**
>**-: 设置内容和标题栏居右对齐。**
**:- 设置内容和标题栏居左对齐。**
**:-: 设置内容和标题栏居中对齐。**

演示：
| 左对齐 | 右对齐 | 居中对齐 |
| :-----| ----: | :----: |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |
---
# Markdown高级技巧
#### 支持的HTML元素
不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。
目前支持的 HTML 元素有：\<kbd> \<b> \<i> \<em> \<sup> \<sub> \<br>等 

示例：
>使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑
#### 转义
使用‘ \ ’可取消转义

#### 公式
Markdown Preview Enhanced 使用 KaTeX 或者 MathJax 来渲染数学表达式。

KaTeX 拥有比 MathJax 更快的性能，但是它却少了很多 MathJax 拥有的特性。你可以查看 KaTeX supported functions/symbols 来了解 KaTeX 支持那些符号和函数。

默认下的分隔符：
>\$...$ 或者 \(...\) 中的数学表达式将会在行内显示。
\$$...$$ 或者 \[...\] 或者 ```math 中的数学表达式将会在块内显示。

![动图演示](https://img-blog.csdnimg.cn/img_convert/76e72d7caa25f9a493b07218f9e43d71.gif)


---
# 文本操作
>基础知识：
Markdown 通过简单标记语法，使普通文本内容具有一定格式。但它本身不支持修改字体、字号与颜色等功能的。CSDN-markdown 编辑器是其衍生版本，支持基于 PageDown ( Stack Overflow）所使用的编辑器的扩展功能（如表格、脚注、内嵌HTML、内嵌 LaTeX 等等）。
Size：规定文本的尺寸大小，取值从 1 到 7 ，浏览器默认值是 3

#### 1.更改字体、大小、颜色
Markdown语法：
```
<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=red>我是红色</font>
<font color=#008000>我是绿色</font>
<font color=Blue>我是蓝色</font>
<font size=5>我是尺寸</font>
<font face="黑体" color=green size=5>我是黑体，绿色，尺寸为5</font>
```
效果如下：<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=red>我是红色</font>
<font color=#008000>我是绿色</font>
<font color=Blue>我是蓝色</font>
<font size=5>我是尺寸</font>
<font face="黑体" color=green size=5>我是黑体，绿色，尺寸为5</font>

#### 2.为文字添加背景色
>由于 style 标签和标签的 style 属性不被支持，所以这里只能是借助 table, tr, td 等表格标签的 bgcolor 属性来实现背景色。故这里对于文字背景色的设置，只是将那一整行看作一个表格，更改了那个格子的背景色（bgcolor）

Markdown语法
```
<table><tr><td bgcolor=yellow>背景色yellow</td></tr></table>
```
效果如下：
<table><tr><td bgcolor=PowderBlue>背景色PowderBlue</td></tr></table>

>色调选择请参考 [hug](https://blog.csdn.net/weixin_34355715/article/details/90152991?utm_medium=distribute.pc_feed_404.none-task-blog-2~default~BlogCommendFromBaidu~Rate-1.pc_404_mixedpudn&depth_1-utm_source=distribute.pc_feed_404.none-task-blog-2~default~BlogCommendFromBaidu~Rate-1.pc_404_mixedpud)
---
以上学习来自于[菜鸟教程]及[blog2](https://blog.csdn.net/heimu24/article/details/81189700)

  [1]: http://www.google.com/
  [菜鸟教程]:https://www.runoob.com/markdown/md-tutorial.html
  [blogs]: https://blog.csdn.net/qq_56914146?type=blog
