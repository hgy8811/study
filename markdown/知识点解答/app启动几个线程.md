## APP 启动几个线程

3个：主线程&两个Binder线程

每个App进程中至少会有两个binder线程 ApplicationThread(简称AT)和ActivityManagerProxy（简称AMP）

一个主动调用/一个被动调用

```java
final ApplicationThread mAppThread = new ApplicationThread();
/////////////////android 6.0 源码///////////////
Looper.prepareMainLooper();
ActivityThread thread = new ActivityThread();
thread.attach(false);
Looper.loop();
///////////////////////
private void attach(boolean isSystem){
  //....
  final IActivityManager mgr = ActivityManagerNative.getDefault();
  mgr.attachApplication(mAppThread)
  //.....
}

```
