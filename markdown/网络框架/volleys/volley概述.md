## Volley 概述

我们在主线程中调用RequestQueue的add()方法来添加一条网络请求，这条请求会先被加入到缓存队列当中，如果发现可以找到相应的缓存结果就直接读取缓存并解析，然后回调给主线程。如果在缓存中没有找到结果，则将这条请求加入到网络请求队列中，然后处理发送HTTP请求，解析响应结果，写入缓存，并回调主线程。


CacheDispatcher     先进行缓存判断

NetworkDispatcher   进行网络请求

KGImageNetwork -> 最终访问网络的是我们自己的KGHttpClient



ImageLoader 二级缓存： 内存缓存+硬盘缓存


## Volley 的优点

非常适合进行数据量不大，但通信频繁的网络操作
可直接在主线程调用服务端并处理返回结果
可以取消请求，容易扩展，面向接口编程
网络请求线程NetworkDispatcher默认开启了4个，可以优化，通过手机CPU数量
通过使用标准的HTTP缓存机制保持磁盘和内存响应的一致
## Volley 的缺点

使用的是httpclient、HttpURLConnection
6.0不支持httpclient了，如果想支持得添加org.apache.http.legacy.jar
对大文件下载 Volley的表现非常糟糕
只支持http请求
图片加载性能一般

只能加载网络图片

作者：SavySoda
链接：https://www.jianshu.com/p/33be82da8f25#good
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
