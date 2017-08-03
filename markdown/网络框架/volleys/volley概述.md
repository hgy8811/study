## Volley 概述

我们在主线程中调用RequestQueue的add()方法来添加一条网络请求，这条请求会先被加入到缓存队列当中，如果发现可以找到相应的缓存结果就直接读取缓存并解析，然后回调给主线程。如果在缓存中没有找到结果，则将这条请求加入到网络请求队列中，然后处理发送HTTP请求，解析响应结果，写入缓存，并回调主线程。


CacheDispatcher     先进行缓存判断

NetworkDispatcher   进行网络请求

KGImageNetwork -> 最终访问网络的是我们自己的KGHttpClient



ImageLoader 二级缓存： 内存缓存+硬盘缓存
