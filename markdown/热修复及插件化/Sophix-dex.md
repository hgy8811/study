# dex

底层替换  + 类加载

底层替换 ： 无视底层具体结构的替换方式，解决兼容性问题ArtMethod  及时生效
类加载： 增量dex + 类的粒度；                        冷启动生效

Dalvik 采用全量dex方案
art 支持多Dex 加载，仅需要把补丁dex作为主dex(classes.dex)加载而已

## Dalvik 下完整DEX方案的新探索

### 一种全新的全量Dex方案
合成完整dex，思路就是把原来的dex和patch里的dex重新合并成一个。

在原先基线包里的dex里面，去掉补丁中也有的class。 这样，补丁+去除了补丁类的基线包，就等于了新app中的所有类
