#-*- coding:utf-8 -*-
# while 循环语句运行后需要终止时需要使用终止语句，一般使用，continue和break
# 1、break用于终止整个循环。
# 2、continue指的是结束这次循环，进入下次循环。
count = 0
while count <=100:
    print('loop:',count)
    if count == 5:
        break
    # 下面的这个语句不执行，后面也不再运行循环了
    count +=1 #result:0,1,2,3,4,5



count1 = 0
while count1 <=100:
    print('loop:',count1)
    if count1 == 5:
        continue
# 则下面这个语句就不会执行了，但是还是会继续下次循环
    count1 +=1  #result:0,1,2,3,4,5,5,5,5...






