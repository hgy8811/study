# Android Studio 中Java文件太长导致无法识别问题 [R.Java文件触发]

需要配置一下android Studio的配置文件即可
首先找到android Studio的安装目录，然后找到bin目录中的idea.properties文件

修改文件中这一行后面的值为9999
idea.max.intellisense.filesize=9999

重启android Studio，就好啦

<font color=red size=3>
Tips： 后面的值应该代表文件大小 单位为K，因为默认是2500，我的R文件2.7M就不能使用了
mac版的android Studio 此文件中默认是没有这一行的，直接添加进去就行了
</font>
