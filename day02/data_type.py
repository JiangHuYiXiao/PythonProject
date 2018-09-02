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



