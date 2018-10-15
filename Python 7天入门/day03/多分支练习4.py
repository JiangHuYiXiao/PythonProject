#-*- coding:utf-8 -*-
# 练习：猜年龄的小游戏
age = 26
guess_age = input('年龄：')
if int(guess_age) == age:
    print('恭喜你猜中了！')
elif int(guess_age) > age:
    print('猜大了，请输入小一点的数据')
elif int(guess_age) < age:
    print('猜小了，请输入大一点的数据')
else:
    print('你输入的年龄有误，请检查后再次输入')