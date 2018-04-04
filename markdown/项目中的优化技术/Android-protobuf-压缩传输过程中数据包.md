
# Android下使用Protobuf进行序列化
发现存在以下问题：

* App中使用Json进行数据传输，存在很多冗余字段的传输，而且经过查阅资料，Json对数据进行序列化以后，数据包仍然很大。
* 柬埔寨存在网络信号问题，很多情况下，信号较差，大数据包的传输存在压力

综合来说，网络环境不稳定和传输数据包过大应该是导致网络请求过程中吃力、或者是超时的主要原因，因此，在优化时，主要考虑如何压缩传输过程中数据包。

## 什么是Protobuf

protobuf，全称：Google Protocol Buffer，是Google开源的一种轻便高效的结构化数据存储格式，可以用于结构化数据的串行化，也称作序列化，主要用于数据存储或是RPC数据交换，支持多语言，可拓展.


protobuf主页： [主页地址](https://developers.google.com/protocol-buffers/)
