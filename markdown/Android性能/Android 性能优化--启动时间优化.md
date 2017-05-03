# Android 性能优化--启动时间优化

## 启动过程内部机制
应用的启动有三种状态，不同状态的启动时长是不一样的。三种状态分别为：冷启动(cold start)，热启动(warm start)，温启动(lukewarm start)。冷启动即应用从零开始加载运行，而其它则是应用从后台运行回到前台运行。

Application -> MainActivity

## 剖析启动性能
Logcat:
I/ActivityManager: Displayed com.android.contacts/.activities.PeopleActivity: +612ms

有两个很好的方法可以用来来定位问题：Method Tracer 工具和 Systrace 工具。


CSDN:http://blog.csdn.net/lgz_ei/article/details/70041663
