# Android深入四大组件（三）广播的注册、发送和接收过程

## 广播的注册过程
BroadcastReceiver的注册分为两种，分别是静态注册和动态注册，静态注册在应用安装时由PackageManagerService来完成注册过程.这里只介绍BroadcastReceiver的动态注册。

ContextWrapper -> ContextImpl -> AMP -> AMS


## 广播的发送和接收过程

### ContextImpl到AMS的调用过程

ContextWrapper[sendBroadcast] -> ContextImpl[sendBroadcast]
-> AMP[broadcastIntent] -> AMS[broadcastIntent/broadcastIntentLocaked]


### AMS到BroadcastReceiver的调用过程

BroadcastQueue的scheduleBroadcastsLocked方法

BroadcastQueue          [scheduleBroadcastsLocked..]
BroadcastQueueHandler   [handleMessage]
ApplicationThread       [performReceive]
InnerReceiver           [performReceive]
ReceiverDispatcher      [performReceive]
Args                    [run]
BroadcastReceiver       [onReceive]
