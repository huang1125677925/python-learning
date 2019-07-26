#!/usr/bin/env bash

#[易百教程]https://www.yiibai.com/sed/sed_regular_expressions.html

#sed输出制定行
sed /pattern/!p infile //匹配pattern的行不输出
sed -n 1,2p infile //print line 1 to 2
sed -n 2,$p file //print line 2 to end of line


#tail 输出格式
#输出从后边查第二行到结束
tail -n 2 log.txt
tail -n -2 log.txt
#输出此文件从前面第十行到结束
tail -n +10 log.txt


#head 输出格式

#输出前面开始第五行之前的部分
head -n 5 log.txt
head -n +5 log.txt
#输出从后边开始到前面的部分
head -n -5 log.txt

#正则表达式
grep -E  '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-([0-9]{4})$' file.txt
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-([0-9]{4})$/' log.txt

#通用的正则表达式
#sed的通用的正则表达式是什么样子？
sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt



