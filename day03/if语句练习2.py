#-*- coding:utf-8 -*-
# 练习3：输入姓名、性别、年龄、判断如果是女生且年龄小于28岁，打印我喜欢女生，否则打印姐弟恋也很好哦。

name = input('姓名:')
sex = input('性别：')
age = input('年龄:')

if sex == '女生' and int(age) < 28:
    print('我喜欢女生')
else:
    print('姐弟恋也很好哦')
