# Binder核心原理与架构设计
1. 性能    数据拷贝一次 相对于socket/消息队列/管道拷贝两次
2. 安全性  相对于传统ipc上层协议保证，有uid/pid进行安全验证
3. 稳定性  C/S通信模式，相对于共享内存，更稳定

Client/Server  Binder driver  ServerMananger 四个角色
