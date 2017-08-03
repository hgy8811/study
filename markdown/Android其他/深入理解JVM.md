# 深入理解JVM

## 深入理解JVM—JVM内存模型
http://www.cnblogs.com/dingyingsi/p/3760447.html
http://www.haonanji.cn/408.html
http://www.jb51.net/article/88963.htm

主内存+工作内存
围绕： 原子性、可见性、有序性

## JVM对象引用与内存分配策略
http://blog.csdn.net/huachao1001/article/details/51547290
tips: 新生代gc用复制算法空间换时间所以比较快，老年代gc用复制压缩算法时间换空间所以比较慢


方法区、程序计数器、虚拟机栈、虚拟机堆、本地方法栈

线程独有：操作数栈、程序计数器、栈
线程共享：常量池、堆、方法区
