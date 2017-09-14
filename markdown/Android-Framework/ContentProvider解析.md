# ContentProvider 解析

1. ContextImpl.getContentResolver()  返回的mContentProvider 在ContextImplg构造函数里初始化

2. ContentResolver.acquireProvider() 即: ApplicationContentResolver.acquireProvider()

 -> mMainThread.acquireProvider()
 -> mMainThread.acquireExistingProvider
 -> ActivityManagerNative.getDefault().getContentResolver()
 -> mMainThread.installProvider()

 ContentProvider.getIContentProvider() 返回Binder对象，对服务端ContentProvider的引用

 
