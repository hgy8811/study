# 当前各种热补丁框架对比 & Tinker 的设计目标

## AndFix
Andfix 是阿里推出的开源框架，它在 github 的地址是：
https://github.com/alibaba/AndFix

技术原理：采用 native hook 的方式，这套方案直接使用 dalvik_replaceMethod 替换 class 中方法的实现

缺点：
* 兼容性不佳；由于它采用 native 替换的方式，在 github Issue 中也有大量崩溃的反馈
* 成功率不高；不支持修改 inline 方法，不支持修改方法参数超过8个或参数中带有 long, double 或者 float。跟一些使用 Andfix 的产品讨论过，它们的成功率不超过40%；
   原因： 只替换了 DexCache 中的 ArtMethod 结构体，对于 Art 中一些 compiledCode 是直接通过 bx 过去
* 开发不透明； 由于它还不支持增加 field，我们需要为了补丁而补丁，无法采用这个技术发布需求。

Andfix 的好处是可以立刻生效，但它可以支持的补丁场景非常有限，仅仅可以使用它来修复特定问题。

## Qzone 超级补丁方案

这个方案使用 classloader 的方式，能实现更加友好的类替换。而且这与我们加载 Multidex 的做法相似，能基本保证稳定性与兼容性。
它主要的面临问题有两个:
* 为了解决 unexpected DEX problem 异常，而采用插桩的方式给所有类插入不会真正运行的代码，防止类打上 preverify 标志。
  采用插桩导致所有类都非 preverify，导致 verify 与 optimize 操作会在加载类时触发。这会有一定的性能损耗.

* 在 art 平台，若补丁中的类出现 Field、Method 或 Interface 变化，可能会导致出现内存地址错乱的问题。为了解决这个问题，我们最后补丁中的类要有 以下规则：
  a. 修改跟新增的 class；
  b. 若 class 有 field，method 或 interface 数量变化，它们所有的子类；
  c. 若 class 有 field，method 或 interface 数量变化，它们以及它们所有子类的调用类。如果采用 ClassN 方式，即需要多个 dex 一起处理。

Qzone 的方案最为简单，而且开发透明，补丁的成功率也是非常高的。
但由于微信对于运行性能以及补丁大小 都比较敏感，我们最终也没有采用这套方案。
