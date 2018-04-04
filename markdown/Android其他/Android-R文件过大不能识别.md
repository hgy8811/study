# R文件过大导致识别不了的问题

最近的R文件过大导致识别不了的问题，可以去修改AS安装目录下的bin目录的idea.properties，改大idea.max.intellisense.filesize 这一行的值，比如9999，
修改完完全退出AS再进入应该就可以了
