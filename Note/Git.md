# Git常用命令
1. 创建空目录
```
$ mkdir <Path>
$ cd <Path>
$ pwd
```

2. 初始化仓库
```
$ git init
```
3. 将文件添加到仓库
```
$ git add <file>
```
4. 提交更改到仓库
```
$ git commit -m <"note">
```
5. 查看工作区的状态
```
$ git status
```
6. 查看文件修改情况
```
$ git diff <file>
```
7. 查看commit记录
```
$ git log
```
8. 回退到上一个版本
```
$ git reset --hard HEAD^
```
9. 回退到指定版本
```
$ git reset --hard <commit_id>
```
10. 查看每一次命令(可以看到提交号)
```
$ git reflog
``` 
11. 丢弃工作区的修改(其实是用版本库里的文件替换工作区)
```
$ git checkout -- <file>
```
12. 丢弃暂存区的修改
```
$ git reset HEAD <file>
```
13. 在版本库删除文件(记得commit)
```
$ git rm <file>
```
14. 创建ssh-key
```
$ ssh-keygen -t rsa -C "youremail@example.com"
```
15. 关联远程库
```
$ git remote add origin git@github.com:ValentineF/TuzkiCode.git
```
16. 把本地库推送到远程库(第一次添加-u，之后就不用了)
```
$ git push -u origin master
```
17. 克隆远程库
```
$ git clone git@github.com:ValentineF/TuzkiCode.git
```
18. 创建并切换到分支
```
//创建并切换
$ git checkout -b dev
```
```
//创建分支
$ git branch dev
//切换分支
$ git checkout dev
```
19. 查看分支
```
$ git branch
```
20. 合并分支
```
$ git merge <branch>
```
21. 删除分支
```
$ git branch -d <branch>
```
22. 抓取分支
```
$ git pull
``` 
# Git常识
1. Head   
在Git中，用HEAD表示当前版本，也就是最新的提交3628164...882e1e0（注意我的提交ID和你的肯定不一样），上一个版本就是HEAD^，上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100
2. 分区   
分为工作区，版本库（内有暂存区和分支），add命令就是把工作区的文件放到暂存区，commit则是提交到分支。
3. 分布式和集中式   
Git为分布式管理，SVN为集中式管理；   
Git下每个人都是一个完整的库；SVN则类似与图书馆
# 命令图
![](https://github.com/ValentineF/TuzkiCode/blob/master/Resource/GitCommand.png)    