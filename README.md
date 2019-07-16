# python-learning

不断总结和晚上各个方面的内容、知识点、代码。
## 编程规范
编程过程中需要注意的事项

命名规范

开发技巧

## 读书笔记文档

## 分布式

## 机器学习算法



## 基本数据类型及容器

List、dict、set、tuple

Counter、Deque、


## 基础知识

## 面向对象

## 日志收集

## 数据处理第三方库

## 算法

## 通信

## 消息读写
1. 从kafka读写；
2. 从mysql读写；
3. 从mongodb读写；
4. 从redis读写；
## 协程进程线程

## 装饰器

## git

git是代码管理不可缺少的工具，git的学习也不是一蹴而就的，需要对git进行仔细的学习。

[git stash](https://blog.csdn.net/daguanjia11/article/details/73810577)
使用git stash 缓存当前工作，然后切换到其他分分支，之前一直不知道这个stash缓存之后，回到当前分支后还需要恢复一下，
导致代码就不见了。

[git log](https://blog.csdn.net/daguanjia11/article/details/73823617)
日志的用法

[廖雪峰的git](https://www.liaoxuefeng.com/wiki/896043488029600/897889638509536)非常好的资料
1. 如果改变没有添加到暂存区，那么可以用`git checkout -- file`可以丢弃工作区的修改
2. 如果改变已经添加到暂存区，那么可以用`git reset HEAD <file>`可以把暂存区的修改撤销掉（unstage),然后再清除工作区
3. 