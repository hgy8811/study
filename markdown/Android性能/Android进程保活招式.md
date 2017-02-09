# Android进程保活

```
Android进程保活包括两个层面：

1. 提供进程优先级，降低进程被杀死的概率

2. 在进程被杀死后，进行拉活
```

## 进程的优先级
根据进程的重要性，被划分为5级：

1. 前台进程 (Foreground process)
2. 可见进程 (Visible process)
3. 服务进程 (Service process)
4. 后台进程 (Background process) 对不可见的Activity的进程（已调用onStop()方法）
5. 空进程 (Empty process)    保留的唯一目的是用作缓存

## 进程的回收策略
主要依靠LowMemorykiller来完成，是一种根据OOM_ADJ阈值级别触发相应力度的内存回收的机制。

## 提升进程优先级的方案


## 进程死后拉活的方案

## 其他有效拉活方案
