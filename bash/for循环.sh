#!/usr/bin/env bash
#TODO：
a=10
b=20
#if [ $a == $b ]
if test $[a] -eq $[b]
then
   echo "a 等于 b"
elif [ $a -gt $b ]
then
   echo "a 大于 b"
elif [ $a -lt $b ]
then
   echo "a 小于 b"
else
   echo "没有符合的条件"
fi


num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2]
then
    echo '两个数字相等!'
else
    echo '两个数字不相等!'
fi


for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done


int=1
while(( $int<=10 ))
do
    echo $int
    let "int++"
done
#Bash let 命令，它用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量


#echo '按下 <CTRL-D> 退出'
#echo -n '输入你最喜欢的网站名: '
#while read FILM
#do
#    echo "是的！$FILM 是一个好网站"
#done

#无限循环

#while :
#do
#    command
#done
#
#while true
#do
#    command
#done
#
#for (( ; ; ))
