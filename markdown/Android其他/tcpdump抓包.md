# tcpdump抓包文档相关

备注：需要有root权限的手机

tcpdump下载地址：
（该版本可解决4.4以上系统报错：error: only position independent executables (PIE) are supported.）
https://github.com/zencodex/hack-android/raw/master/arm-bin/tcpdump-pie/tcpdump

教程：
http://www.trinea.cn/android/tcpdump_wireshark/

1. 下载并安装tcpdump
下载地址：tcpdump（该版本在Android4.4会出问题，原因以及解决：http://m.oschina.net/blog/468757）

安装tcpdump，命令行模式依次执行：
adb root
adb push /Users/huguoyin/Desktop/移动包月/tcpdump /data/local/tcpdump
adb shell chmod 6755 /data/local/tcpdump

其中adb push的第一个参数为本地tcpdump的路径。

2. 启动并运行tcpdump
命令行模式运行下面命令：
adb shell /data/local/tcpdump -n -s 0
这时在手机上做任何涉及到网络的操作都会在屏幕上打印出来，可以通过ctrl+c停止。

由于命令行最大输出的限制及屏幕不断滚动，查看不方便，我们可以将抓取的网络包保存到sd卡，如下命令：
adb shell /data/local/tcpdump -i any -p -s 0 -w /sdcard/test1.pcap

依然通过ctrl+c停止，将文件拉取到本地PC
adb pull /sdcard/test1.pcap C:\Users\huguoyin\Desktop\test1.pcap （windows）
adb pull /sdcard/test1.pcap /Users/huguoyin/Desktop/移动包月/test1.pcap  （mac）

3. 利用wireshark分析数据

用wireshark打开capture.pcap即可分析log
关于wireshark具体可见：http://www.cnblogs.com/TankXiao/archive/2012/10/10/2711777.html
