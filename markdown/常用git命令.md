# 常用Git命令

* 通过--no-merges标记来排除merge提交：
git log --no-merges

* 使用--merges标记只看merge提交
git log --merges

* 根据commiter过滤该用户的所有提交

 git log --pretty=oneline --author="xxxx"


exp:
git log --no-merges --pretty=oneline --author="xxx"
