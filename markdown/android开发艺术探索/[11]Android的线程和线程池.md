# Android的线程和线程池

Thread、AsyncTask、IntentService、HandlerThread

线程受限，不能无限产生，并且线程的创建和销毁都会有相应的开销。线程池！！

## AsyncTask

## HandlerThread

## IntentService

封装了HandlerThread和Handler

## android中的线程池
优点：
1. 重用线程，避免线程的创建和销毁所带来的性能开销
2. 控制线程池的最大并发数，避免大量的线程之间抢占系统资源而导致阻塞现象。
3. 对线程进行简单的观看，提供定时执行及指定间隔循环执行等功能。

核心线程->任务队列-> 非核心线程 -> 拒绝处理回调

### FixedThreadPool
只有核心线程，都处于活动状态并且不会被回收

适合快速响应外界的请求
### CacheThreadPool
线程数量不定的线程池，只有非核心线程，最大数为Integer.MAX_VALUE
任何任务都会立即执行，相当于没有任务队列

适合用来执行大量的耗时较少的任务。
### ScheduleThreadPool
核心线程数量是固定的，非核心线程数是没有限制的

适合执行定时任务和具有固定周期的重复任务
### SingleThreadExecutor

只有一个核心线程，确保所有的任务都在同一个线程中按顺序执行。

适合顺序串行执行的任务
