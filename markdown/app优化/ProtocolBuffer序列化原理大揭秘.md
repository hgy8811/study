# Protocol Buffer 序列化原理大揭秘 - 为什么Protocol Buffer性能这么好？

http://blog.csdn.net/carson_ho/article/details/70568606

## 前言

* 习惯用 Json、XML 数据存储格式的你们，相信大多都没听过Protocol Buffer
* Protocol Buffer 其实 是 Google出品的一种轻量 & 高效的结构化数据存储格式，性能比 Json、XML 真的强！太！多！

* 今天，我将讲解为什么Protocol Buffer的性能如此的好：
a. 序列化速度 & 反序列化速度快
b. 数据压缩效果好，即序列化后的数据量体积小

## 总结
在 传输数据量较大的需求场景下，Protocol Buffer比XML、Json 更小、更快、使用 & 维护更简单！
