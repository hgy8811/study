## PMS 安装APK
安装过程会对dex进行优化

最后调用performDexOptLI对APK安装包中的dex文件做优化，当然这里会依据当前是采用DVM还是ART的运行环境，分别用dexopt和dex2oat两种不同的命令对classes.dex文件做优化并存储在/data/dalvik-cache下面的文件里，关于dex文件优化的部分，可以参考一下Android虚拟机相关知识。

PackageDexOptimizer.java  -> performDexOptLI
