## 常见的异常

资源找不到  ->  {覆盖安装} -> 通知栏需要的资源进行资源id固化

res/values/public.xml 进行资源id固化
## 找资源
通知栏由系统进程控制 -> 支持基础的控件，不支持自定义
通过apk包名及资源id 找resource


## 监听被清除
 Notification.Builder setDeleteIntent
