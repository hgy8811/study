# WindowManagerService [深入理解Android卷三]

那么，窗口的本质是什么呢？
是进行绘制所使用的画布：Surface。
当一块Surface显示在屏幕上时，就是用户所看到的窗口了。客户端向WMS添加一个窗口的过程，其实就是WMS为其分配一块Surface的过程，一块块Surface在WMS的管理之下有序地排布在屏幕上，Android才得以呈现出多姿多彩的界面来。所以从这个意义上来讲，WindowManagerService被称之为SurfaceManagerService也说得通的。
于是，根据对Surface的操作类型可以将Android的显示系统分为三个层次，如图4-2所示。

·  第一个层次是UI框架层，其工作为在Surface上绘制UI元素以及响应输入事件。
·  第二个层次为WMS，其主要工作在于管理Surface的分配、层级顺序等。
·  第三层为SurfaceFlinger，负责将多个Surface混合并输出。
