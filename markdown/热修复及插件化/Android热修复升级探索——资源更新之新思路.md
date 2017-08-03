# Android热修复升级探索——资源更新之新思路

https://yq.aliyun.com/articles/96378

目前市面上的很多资源热修复方案基本上都是参考了Instant Run的实现。
Instant Run资源热修复的核心代码就是这个monkeyPatchExistingResources方法：

简要说来，Instant Run中的资源热修复分为两步：

1、构造一个新的AssetManager，并通过反射调用addAssetPath，把这个完整的新资源包加入到AssetManager中。这样就得到了一个含有所有新资源的AssetManager。

2、找到所有之前引用到原有AssetManager的地方，通过反射，把引用处替换为AssetManager。

一般来说，一个resources.arsc里面包含若干个package，不过默认情况下，由打包工具aapt打出来的包只有一个package。这个package里包含了app中的所有资源信息。

资源信息主要是指每个资源的名称以及它对应的编号，编号是一个32位数字，用十六进制来表示就是0xPPTTEEEE。PP为package id，TT为type id，EEEE为entry id。

## 运行时资源的解析
默认由Android SDK编出来的apk，是由aapt工具进行打包的，其资源包的package id就是0x7f。
系统的资源包，也就是framework-res.jar，package id为0x01。
在走到app的第一行代码之前，系统就已经帮我们构造好一个已经添加了安装包资源的AssetManager了。这个AssetManager里就已经包含了系统资源包以及app的安装包，就是package id为0x01的framework-res.jar中的资源和package id为0x7f的app安装包资源。

如果此时直接在原有AssetManager上继续addAssetPath的完整补丁包的话，由于补丁包里面的package id也是0x7f，就会使得同一个package id的包被加载两次。这会有怎样的问题呢？

* 在Android L之后，这是没问题的，他会默默地把后来的包添加到之前的包的同一个PackageGroup下面。而在解析的时候，会与之前的包比较同一个type id所对应的类型，如果该类型下的资源项数目和之前添加过的不一致，会打出一条warning log，但是仍旧加入到该类型的TypeList中。

在获取某个Type的资源时，会从前往后遍历，也就是说先得到原有安装包里的资源，除非后面的资源的config比前面的更详细才会发生覆盖。而对于同一个config而言，补丁中的资源就永远无法生效了。所以在Android L以上的版本，在原有AssetManager上加入补丁包，是没有任何作用的，补丁中的资源无法生效。

* 而在Android KK及以下版本，addAssetPath只是把补丁包的路径添加到了mAssetPath中，而真正解析的资源包的逻辑是在app第一次执行AssetManager::getResTable的时候。
而在执行到加载补丁代码的时候，getResTable已经执行过了无数次了。这是因为就算我们之前没做过任何资源相关操作，Android framework里的代码也会多次调用到那里。所以，以后即使是addAssetPath，也只是添加到了mAssetPath，并不会发生解析。所以补丁包里面的资源是完全不生效的！

所以，像Instant Run这种方案，一定需要一个全新的AssetManager时，然后再加入完整的新资源包，替换掉原有的AssetManager。

## 另辟蹊径
而一个好的资源热修复方案是怎样的呢？
首先，补丁包要足够小，像直接下发完整的补丁包肯定是不行的，很占用空间。

而像有些方案，是先进行bsdiff，对资源包做差量，然后下发差量包，在运行时合成完整包再加载。这样确实减小了包的体积，但是却在运行时多了合成的操作，耗费了运行时间和内存。合成后的包也是完整的包，仍旧会占用磁盘空间。

而如果不采用类似Instant Run的方案，市面上许多实现，是自己修改aapt，在打包时将补丁包资源进行重新编号。这样就会涉及到修改Android SDK工具包，即不利于集成也无法很好地对将来的aapt版本进行升级。

<font color=red>针对以上几个问题，一个好的资源热修复方案，既要保证补丁包足够小，不在运行时占用很多资源，又要不侵入打包流程。我们提出了一个目前市面上未曾实现的方案。</font>
