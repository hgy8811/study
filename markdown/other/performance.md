# 性能优化

## 流畅度
GPU呈现模式、blockCanary、ActivityThread主线程Looper监控

线程太多 也会降低性能，泛滥也不是好事

抢占CPU资源，导致UI线程执行时间少

频繁GC stw (stop the world)
