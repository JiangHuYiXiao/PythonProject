#-*- coding:utf-8 -*-
# 计算机的运算按照种类分，可以分为算数运算、比较运算、逻辑运算、赋值运算、成员运算、身份运算、位运算。

# 算术运算
# 加+
a = 10
b = 20
print(a + b)
#减-
print(a-b)
# 乘*
print(a*b)
# 除/
print(b/a)
# 取余%
print(b%a)
# 幂运算**
print(a**2)
# 取整除的数//
print(b//3)

# 比较运算，比较运算的结果是布尔值（true or false）

# ==比较两个对象是否相等
print(a == b)

# 不等于！= 或者<>
print(a != b)
# print(a <> b) 这个运算符只有python2支持，python3不支持

# 大于 >
print(b > a)
# 小于<
print(a < b)
#小于等于<=
print(a <= b)
# 大于等于>=
print(b >= a)

# 赋值运算

# 简单的赋值运算符=
c = a + b
print(c)
# 加法赋值+=
a +=b  #a = a + b
print(a)
# 减法赋值-=
a -= b #a = a - b
print(a)
# 乘法赋值
a *= b #a = a*b
print(a)
#除法赋值
a /= b #a = a/b
print(a)


# 逻辑运算
# and：与，两个条件都成立为true
# or ：或，两个条件一个成立为true
# not：非，true的非为false，false的非为true
d = 10
f = 20
print(a == 10 and b == 20)#true
print(a == 10 or b == 30)#true
print(not(a == 20 or b == 40)) #true


