## Android 性能优化

1===================
渲染机制
内存及GC
电量优化
2===================
电量优化
网络优化
对象池提高效率
LRU Cache
Bitmap的缩放、缓存、重用 PNG压缩
自定义View的性能、提升设置alpha之后的View渲染性能
lint、StrickMode等工具的使用
3===================
更高效的容器 arraymap、SparseArray和Pair
onLowMemory与onTrimMemory的回调与内存泄漏
重复 layout 操作的性能影响
使用 Batching，Prefetching 优化网络请求，压缩传输数据等使用技巧
4===================
优化网络请求的行为
优化安装包的资源文件
优化数据传输的效率
性能优化的几大基础原理
5===================
多线程并发的性能
tips:线程池 统一管理和创建
AsyncTask：默认线性调度、cancel方法不靠谱、是内部类存在生命周期管理问题、
HandlerThread：Looper(线程存活并取任务执行)、Handler(管理队列任务添加取消)、MessageQueue(任务载体容器)；线程优先级的设置
ThreadPool：统一管理；Runtime.getRuntime().availableProcesser()方法并不可靠，他返回的值并不是真实的CPU核心数，因为CPU会在某些情况下选择对部分核心进行睡眠处理，在这种情况下，返回的数量就只能是激活的CPU核心数。
IntentService：内置的是HandlerThread作为异步线程

Loader的出现就是为了确保工作线程能够和Activity的生命周期保持一致；从Android M系统更新了GPU Profiling的工具来帮助我们定位UI的渲染性能问题。
增加并发的线程数会导致内存消耗的增加，平衡好这两者的关系是非常重要的，不要在任何非UI线程里面去持有UI对象的引用，
6===================
程序启动时间性能优化->优化activity创建，优化Application对象的启动，正确使用启动显屏达到优化程序启动性能的目的
减少安装包大小的 checklist 以及如何使用 VectorDrawable 来减少安装包的大小
