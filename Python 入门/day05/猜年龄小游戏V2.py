#-*- coding:utf-8 -*-
# 练习：优化猜年龄小游戏，允许用户猜三次，中间猜对了，直接跳出循环。
# 猜了三次后，再问是否还想玩，如果用户选Y，则再允许猜三次，以此反复。
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
    if count ==4:
        choice = input('你个笨蛋,请问是否还要继续，选择y/Y继续猜')
        if choice == 'y' or choice == 'Y':
            count = 1

