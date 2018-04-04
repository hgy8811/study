# Android应用程序进程启动过程
http://liuwangshu.cn/framework/applicationprocess/1.html
## 应用程序进程概述
要想启动一个应用程序，首先要保证这个应用程序所需要的应用程序进程已经被启动。ActivityManagerService在启动应用程序时会检查这个应用程序需要的应用程序进程是否存在，不存在就会请求Zygote进程将需要的应用程序进程启动。

## 应用程序进程创建过程

### 发送创建应用程序进程请求
ActivityManagerService会通过调用startProcessLocked函数来向Zygote进程发送请求，如下所示。
frameworks/base/services/core/java/com/android/server/am/ActivityManagerService.java

## 在应用程序进程创建过程中会启动Binder线程池以及在应用程序进程启动后会创建消息循环
