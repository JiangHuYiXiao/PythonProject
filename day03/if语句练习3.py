#-*- coding:utf-8 -*-
# 练习3：输入姓名、性别、年龄、判断如果是女生且年龄小于28岁，打印我喜欢女生，否则打印姐弟恋也很好哦,如果是男生，打印一起来搞基。

name = input('姓名:')
sex = input('性别：')
age = input('年龄:')

if sex == '女生':
    if int(age) < 28:
        print('我喜欢女生')
    else:
        print('姐弟恋也很好哦')
if sex == '男生':
    print('一起来搞基')
