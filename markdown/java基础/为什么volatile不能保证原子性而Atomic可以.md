## 为什么volatile不能保证原子性而Atomic可以

http://www.cnblogs.com/Mainz/p/3556430.html



volatile只能保证可见性及有序性，先读后写，在你写之前别人可能也在写，没法防止并发。
至于AtomicInteger，首先有volatile value保证变量的可见性，再借助了CPU级指令CAS保证了原子性。
