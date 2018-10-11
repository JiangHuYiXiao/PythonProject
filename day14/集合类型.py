#-*- coding:utf-8 -*-
# 集合是一个无序的，不重复的数据集合
# 作用：
# 1、去重
# 2、进行关系测试，交集，差集，并集，子集，超集，等。

# 1、定义
s = {}
print(type(s))   #<class 'dict'>空时就是字典，有数据时是集合

s ={1,3,32,22,2}
print(type(s))    #<class 'set'>

# 2、去重
s = {1,2,3,3}   #定义的时候存在重复，引用时已经去重
print(s)  #{1, 2, 3}

# 3、其他数据类型转换成集合(只能将列表或者元组转成集合)
list =[1,2,4,22,445]
print(set(list))

tuple = (2,3,4)
print(set(tuple))


# 集合的方法
# 增加 .add
s1 = {1,2,3,444,333,'jianghu'}
s1.add(1) #放一个已经存在的放入不了
s1.add(100)
print(s1)

# 删除 .pop() ,.remove
s1.pop()
print(s1)

s1.remove(2)
print(s1)

# remove删除已经不存在的会报错
# s1.remove(1)
# print(s1)

s1.discard(1)  #discard删除已经不存在的不会报错
print(s1)

# update
s1.update([22,888,1000])
print(s1)    #{3, 100, 1000, 333, 'jianghu', 22, 888, 444}

#清空
s1.clear()
print(s1)