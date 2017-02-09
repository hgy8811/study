# Android 严苛模式（StrictMode）

## 什么是StrictMode

官方解释：http://developer.android.com/intl/zh-cn/reference/android/os/StrictMode.html

Tips:严苛模式是一个开发工具，能够检测程序中的违例，从而修复。最常用的地方检测主线程中disk读写和网络请求等耗时操作。目前能有两大策略:线程策略（ThreadPolicy）和Vm策略（VmPolicy）。

## 如何使用

严格模式的开启可以放在Application或者Activity以及其他组件的onCreate方法。为了更好地分析应用中的问题，建议放在Application的onCreate方法中。

```java
public void onCreate() {
    if (DEVELOPER_MODE) {
        StrictMode.setThreadPolicy(new StrictMode.ThreadPolicy.Builder()
                .detectDiskReads()
                .detectDiskWrites()
                .detectNetwork()   // or .detectAll() for all detectable problems
                .penaltyLog()
                .build());
        StrictMode.setVmPolicy(new StrictMode.VmPolicy.Builder()
                .detectLeakedSqlLiteObjects()
                .detectLeakedClosableObjects()
                .penaltyLog()
                .penaltyDeath()
                .build());
    }
    super.onCreate();
}
```

## 如何配置

我们可以通过建造者模式去灵活配置。

### ThreadPolicy

* detectAll 检测所有潜在的违例
* detectCustomSlowCalls 自定义耗时操作
* detectDiskReads 读磁盘操作
* detectDiskWrites 写磁盘操作
* detectNetwork    网络操作
* detectResourceMismatches 检测资源类型是否匹配

### VmPolicy

* detectAll 检测所有潜在的违例
* detectActivityLeaks 检测Activity的泄露
* detectCleartextNetwork 检测明文的网络
* detectFileUriExposure  检测file://或者是content://
* detectLeakedClosableObjects 检测未关闭的Closable对象泄露，如流没有关闭
* detectLeakedRegistrationObjects 检测需要注册类型是否解注
* detectLeakedSqlLiteObjects 检测SQLiteCursor泄漏

## 检测到违规项之后的表现形式

* penaltyDeath   //检测到问题时，直接崩溃
* penaltyDeathOnNetwork crash,在所有值钱，必须调用detectNetwork去允许这个。
* penaltyDialog 弹出dialog
* penaltyDropBox 将日志吸入到dropbox中
* penaltyFlashScreen 屏幕闪烁
* penaltyLog    //检测到问题时，将日志输出到Logcat

## 查看结果

```
adb logcat | grep StrictMode

```

## 总结

* 严格模式需要在debug模式开启，不要在release版本中启用。
* StrictMode非常有用，会将应用的违例细节暴露给开发者方便优化与改善，相对轻松的解决部分性能问题。
