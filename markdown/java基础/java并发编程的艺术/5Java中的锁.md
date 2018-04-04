# Java中的锁

## Lock/ReentrantLock(可重入锁)

```java

Lock lock = new ReentrantLock();
lock.lock();
try{
}finally{
  lock.unlock();
}
```
在finally块中释放锁，目的是保证在获取锁之后，最终能够释放锁。不要将获取锁的过程写在try块中，因为如果在获取锁时发生了异常，异常抛出的同时，也会导致锁无故释放。

Lock接口提供synchronized关键字所不具备的特性：
* 尝试非阻塞获取锁
* 能被中断地获取锁
* 超时获取锁

page 237

## 共享式同步状态获取与释放

共享式获取与独占式获取最主要的区别在于同一时刻能否有多个线程同时获取同步状态。
