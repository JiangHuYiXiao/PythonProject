#-*- coding:utf-8 -*
# while else循环主要是用于判断我们的while循环过程中是否出现中断情况，如果中间循环出现中断则不会执行else语句
# 只会执行到while循环为止。
# 可以在else里面输出一些日志等提示信息。

count = 0
while count <=5:

    print('loop:',count)
    count += 1
    if count == 3:
        break

else:
    print('循环出现终止，请检查!')

