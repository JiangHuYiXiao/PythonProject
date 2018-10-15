#-*- coding:utf-8 -*-
# python默认是17位的精度，也就是小数点后16位，但是这个精确度越到后面越不准，
# 其他语言也存在同样的问题，这个是和浮点数的存储结构有问题。

# 计算高精确度浮点数的办法
# 借助decimal模块的‘getcontext’和‘Decimal’方法
a = 3.14159263513651054608317828332
print(a)#3.1415926351365107
from decimal import *
getcontext().prec = 50 #精度为50
b = Decimal(1) /Decimal(3)
print(b)
print(Decimal(a))