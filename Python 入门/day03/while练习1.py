#-*- coding:utf-8 -*-
# 练习1：打印1到100的偶数
# 方法1
count = 0
while count <=100:
    print ('loop',count)
    count += 2
print('-------end loop ------')

# 方法2
count = 0
while count <= 100:
    if count%2 ==0:
        print('loop',count)
    count += 1




# 循环打印1-100，第50次不打印值，第60-80次打印对应值的平方。

a = 0
while a <=100:

    if a == 50:
        pass #就是过，不打印任何东西
    elif a >= 60  and a <=80:
        print(a*a)
    else:
        print('loop:', a)
    a += 1


