#-*- coding:utf-8 -*-
# python的数据类型可以分为两大类：基本类型、数据集
# 基本类型包含：（数字、字符串、布尔）
# 数据集包含：（列表list、元组tuple、字典dict、集合set）

# 数字：又分为整数int、浮点型float、长整型long
int1 = 2
print(type(int1))# 判断数据类型的方法
# 整数的数据范围为：在32位的机子上是：-2**31~2**32-1，在64位的机子上是：-2**63~2**64-1
minrange = -(2**63)
maxrange = (2**64)-1
print(minrange)
print(maxrange)

float1 = 2.12
print(type(float1))

long1 =1844674407370955161533
print(type(long1)) #结果为int，因为在Python3中所有的长整型都为int，python2中是有long的


# 字符串
# 在python中加了引号的都可以认为是字符串，单引号，双引号，三引号
age1 = 23
print(type(age1))#int

age2 = '23'
print(type(age2))#str

age3 = "I'm age is 23"#单引号和双引号没有任何区别，只有在这种情况下需要一起使用。
print(type(age3))

# age4 = "sdfffdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
#        多行只能用多引号否则报错

# name = jack #没有加引号的字符串被认为是变量，这里会报错，因为变量必须先定义再使用，这边是没有定义jack这个变量

# 定义
jack = 'jackeJiang'

# 使用
name = jack

# 输出结果
print(name)

# 字符串的操作
# 相加
str1 = 'how old are you:'

str2 = '22'

print(str1,str2)

# 相乘
print(str1*2)


# 布尔类型(bool)
# 布尔类型其实就是真（true）假（false），主要用于逻辑判断
a = 10
b = 20
print(a > b)
print(type(a > b))

print(a < b)
print(type(a > b))

