# 应用程序启动过程

http://liuwangshu.cn/framework/component/1-activity-start-1.html

##  Instrumentation
Instrumentation主要用来监控应用程序和系统的交互。


## Launcher到AMS调用过程的时序图

Launcher -> Activity -> Instrumentation -> ActivityManangerProxy -> ActivityManagerService

## ActivityManageService到ApplicationThread的调用流程

ActivityManagerService -> ActivityStarter -> ActivityStackSupervisor -> ActivityStack -> ApplicationThread


## ActivityThread启动Activity

ApplicationThread的scheduleLaunchActivity方法会将启动Activity的参数封装成ActivityClientRecord ，sendMessage方法向H类发送类型为LAUNCH_ACTIVITY的消息.
应用程序进程要启动Activity时需要将该Activity所属的APK加载进来，而LoadedApk就是用来描述已加载的APK文件。

ApplicationThread -> ActivityThread -> H -> Instrumentation -> Activity


<font color=red>
TODO
生命周期详解 需要后续搞懂下！！！
</font>
