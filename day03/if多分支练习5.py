#-*- coding:utf-8 -*-
# 练习：再来匹配个成绩小程序吧，成绩有ABCDE五个等级，与分数的对应关系为：
# A : 90 - 100
# B : 80 - 89
# C : 60 - 79
# D : 40 - 59
# E : 0 - 39

score = int(input('分数：'))
# grade = input('等级：')

if score >=90 and score<=100:
    print('你的成绩等级为：A')
elif score >=80 and score<=89:
    print('你的成绩等级为：B')
elif score >=60 and score<=79:
    print('你的成绩等级为：C')
elif score >=40 and score<=59:
    print('你的成绩等级为：=D')
elif score >=0 and score<=39:
    print('你的成绩等级为：E')
else:
    print('你输入的成绩有误')