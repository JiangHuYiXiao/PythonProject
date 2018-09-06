#-*- coding:utf-8 -*-
# 练习：优化猜年龄小游戏，允许用户最多猜三次，中间猜对了，直接跳出循环。
age = 26

count = 1

while count <=3:
    guess_age = int(input('请输入你猜的年龄：'))
    if guess_age == age:
        print('恭喜你猜中了，可以领走我们的奖品!')
        break
    elif guess_age < age:
        print('请输入更大一点的数据!')
    elif guess_age > age:
        print('请输入更小一点的数据!')
    else:
        print('你输入的数据有误，请修改后再次输入!')
    count += 1



