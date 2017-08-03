# GC Root
常说的GC(Garbage Collector) roots，特指的是垃圾收集器（Garbage Collector）的对象，GC会收集那些不是GC roots且没有被GC roots引用的对象。
一个对象可以属于多个root，GC root有几下种：

* Class - 由系统类加载器(system class loader)加载的对象，这些类是不能够被回收的，他们可以以静态字段的方式保存持有其它对象。我们需要注意的一点就是，通过用户自定义的类加载器加载的类，除非相应的java.lang.Class实例以其它的某种（或多种）方式成为roots，否则它们并不是roots，.
* Thread - 活着的线程
* Stack Local - Java方法的local变量或参数
* JNI Local - JNI方法的local变量或参数
* JNI Global - 全局JNI引用
* Monitor Used - 用于同步的监控对象
* Held by JVM - 用于JVM特殊目的由GC保留的对象，但实际上这个与JVM的实现是有关的。可能已知的一些类型是：系统类加载器、一些JVM知道的重要的异常类、一些用于处理异常的预分配对象以及一些自定义的类加载器等。然而，JVM并没有为这些对象提供其它的信息，因此就只有留给分析分员去确定哪些是属于"JVM持有"的了。

## 内存区域 - 运行时数据区域

* 程序计数器
* java 虚拟机栈
* 本地方法栈
* 方法区
* java 虚拟机堆

## java语言中，可作为GC Roots的对象包括下面几种：

* 虚拟机栈(栈帧中的本地方法表)中引用的对象
* 方法区中类静态属性引用的对象
* 方法区中常量引用的对象
* 本地方法栈中 JNI(Native方法)引用的对象
* Thread ...


## 可达性分析算法

GC Roots 的对象作为起始点，从这些节点开始向下搜索，某个对象不可达则证明不可用

## Java内存模型

* 主内存与工作内存；
* 内存间交互操作；  load store read write
* volatile 型变量的特殊规则；  可见性与禁止指令重排序
* 原子性、可见性、有序性
* 先行发生原则
