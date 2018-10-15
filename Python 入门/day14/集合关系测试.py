#-*- coding:utf-8 -*-
# 1、求交集 intersection
s1 = {11,12,13,14}
s2 = {11,15,16,14,20}
print(s1.intersection(s2))
# 或者 &
print(s1&s2)

# 2、求并集 union
print(s1.union(s2))

# 或者 |
print(s1 | s2)

# 3、差集
print(s1.difference(s2))   #只在s1中的
# 或者 -
print(s1 - s2)
print(s2.difference(s1))   #只在s2中的
# 或者 -
print(s2 - s1)

# 4、取交集相反的（对称差集）只存在于s1或者只存在s2
print(s1.symmetric_difference(s2))

# 5、子集
s2.update([12,13])
print(s2)   #这样s2就包含了s1，s2是s1的超集，s1是s2的子集
print(s2.issubset(s1))  #s2是否是s1的子集 否  False
print(s1.issubset(s2))  #s1是否是s2的子集 是  True

# 或者使用<=
print(s1 <= s2)
print(s2 <= s1)

# 6、超集
print(s2.issuperset(s1))  #s2是否是s1的超集 True
print(s1.issuperset(s2))  #s1是否是s2的超集 False
# 或者使用>=
print(s2 >= s1)
print(s1 >= s2)

# 7、判断两个集合是是不是没有交集
print(s1.isdisjoint(s2))    #False

# 8、把差集的结果赋值给集合s1

s1.update([250,120])
s1.difference_update(s2)
print(s1)  #{120, 250}
print(s2)  #{11, 12, 13, 14, 15, 16, 20}

