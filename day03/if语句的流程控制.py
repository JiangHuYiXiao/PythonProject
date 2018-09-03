#-*- coding:utf-8 -*-
# 单分支：

# if 条件：
#     满足条件后要执行的代码
age = 10
if age < 18:
    print('小于18岁你可以继续浪了')
age = 20
print(age)

# 双分支：

# if 条件：
#     满足条件后执行的代码
# else:
#     if 条件不满足就走这一段代码
age = 20
if age < 18:
    print('小于18岁你可以继续浪了')
else:
    print('小伙子成年了你该懂事了')

#登录判断用if语句
usename = '江湖一笑'
password = '123456'

用户名 = input('用户名：')
密码 = input('密码：')

if usename == 用户名 and password == 密码:
    print('welcome:'+ 用户名)
else:
    print('用户名或者密码错误')




