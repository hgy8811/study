## Glide
Glide是一个非常成熟的图片加载库，他可以从多个源加载图片，如：网路，本地，Uri等，更重要的是他内部封装了非常好的缓存机制并且在处理图片的时候能保持一个低的内存消耗。

优点：

1、图片占用内存回收及时，能减少因内存不足造成的崩溃，生命周期和Activity/Fragment一致。
2、默认Bitmap格式是RGB_565，减少内存资源占用。
3、glide比universal-image-loader占用的内存要小一些。
4、图片显示效果为渐变，更加平滑。
5、glide可以将任何的本地视频解码成一张静态图片。
6、支持 Gif、WebP、缩略图

缺点：

1、glide-3.6.1.jar的大小为465KB，而universal-image-loader-1.9.3.jar大小为157KB。


2. Glide 优点

(1) 图片缓存->媒体缓存
Glide 不仅是一个图片缓存，它支持 Gif、WebP、缩略图。甚至是 Video，所以更该当做一个媒体缓存。



(2) 支持优先级处理



(3) 与 Activity/Fragment 生命周期一致，支持 trimMemory
Glide 对每个 context 都保持一个 RequestManager，通过 FragmentTransaction 保持与 Activity/Fragment 生命周期一致，并且有对应的 trimMemory 接口实现可供调用。



(4) 支持 okhttp、Volley
Glide 默认通过 UrlConnection 获取数据，可以配合 okhttp 或是 Volley 使用。实际 ImageLoader、Picasso 也都支持 okhttp、Volley。

(5) 内存友好
① Glide 的内存缓存有个 active 的设计
从内存缓存中取数据时，不像一般的实现用 get，而是用 remove，再将这个缓存数据放到一个 value 为软引用的 activeResources map 中，并计数引用数，在图片加载完成后进行判断，如果引用计数为空则回收掉。

② 内存缓存更小图片
Glide 以 url、view_width、view_height、屏幕的分辨率等做为联合 key，将处理后的图片缓存在内存缓存中，而不是原始图片以节省大小

③ 与 Activity/Fragment 生命周期一致，支持 trimMemory

④ 图片默认使用默认 RGB_565 而不是 ARGB_888
虽然清晰度差些，但图片更小，也可配置到 ARGB_888。


其他：Glide 可以通过 signature 或不使用本地缓存支持 url 过期
