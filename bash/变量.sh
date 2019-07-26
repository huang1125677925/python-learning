#!/usr/bin/env bash

myUrl="http://www.google.com"
readonly myUrl
echo $myUrl

#删除变量
vari=10
echo $vari
unset vari
echo $vari

your_name='runoob'
str="Hello, I know you are \"$your_name\"! \n"
echo -e $str


your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1
# 使用单引号拼接
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3


