# Android代码替代枚举

在Android官方的性能优化相关课程中曾经提到使用枚举存在的性能问题，不建议在Android代码中使用枚举:

[Enums often require more than twice as much memory as static constants. You should strictly avoid using enums on Android][id]
[id]: https://developer.android.com/topic/performance/memory.html?hl=zh-cn"

## 相比于静态变量：

* 编译后文件体积更大
* 使用时占用更多的内存


## 枚举优点

* 相对于Int静态常量来说，枚举最大的作用是提供了类型安全


## 支持：

* 为了弥补Android平台不建议使用枚举的缺陷，官方推出了两个注解，IntDef和StringDef,用来提供编译期的类型检查

## 结论：

* 仅仅提供类型安全，那么我们可以考虑通过注解来替换；
* 如果我们需要将数据和枚举常量关联起来，在枚举中声明域，然后编写一个带有数据的构造器，可以使用静态类的静态变量 来替代


### 备注引用
** [参考文章 - Android代码替代枚举的正确之道](http://www.jianshu.com/p/f8ac84a3e3c1) **
