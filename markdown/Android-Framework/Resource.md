## resources

Activty.getResource()  ->ContextImpl.getResource()

ContextImpl中的Resource是在其构造函数中进行赋值的
来自 ResourceManager类，它是一个单例类，ArrayMap 存放Resource

ActivityClientRecord/ActivityRecord
LoadedAPK -> 根据包名获取安装apk的相关信息
