#!/usr/bin/env bash
#https://blog.csdn.net/tttyd/article/details/11742241
#https://blog.csdn.net/x1269778817/article/details/46535729
echo $(who)

echo $((3*4))   //算数运算用双小括号

a=10
if ((a < 20))
then
    echo 'a 小于 20'
fi


array=(1 2 3 4)
i=0
while (($i<4))
do
    echo ${array[i]}
    let "i++"
done

echo "数组的元素为: ${array[*]}"
echo "数组的元素为: ${array[@]}"


echo "数组元素个数为: ${#array[*]}"
echo "数组元素个数为: ${#array[@]}"


str='huangchuang'

echo "字符串的长度是： ${#str}"

echo $((16#5f))

a=5
((a++))
echo $a



for i in $(seq 0 4);do echo $i;done
for i in `seq 0 4`;do echo $i;done
for ((i=0;i<5;i++));do echo $i;done
for i in {0..4};do echo $i;done



