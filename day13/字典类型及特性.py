#-*- coding:utf-8 -*-
# 需求：如何在一个变量里面存储一个公司所有员工的个人信息？
names = [['jangtao',18,170,'江西'],['jianghu',34,190,'湖南'],['rain',32,176,'USA'],['Alex',66,145,'广西']]
# 可以通过列表存储，但是怎么获取呢？
# 比若说我要获取jaigntao的个人信息？
# print(names.index('jiangtao')) #ValueError: 'jiangtao' is not in list
# 不可行
# 要么把一整个列表放入进去
print(names.index(['jangtao',18,170,'江西']))  #0

# 这样显然是不可取的，
# 这就引入我们今天要学习的字典
dic1 = {'jiangtao':[18,170,'江西'],'jianghu':[34,190,'湖南'],'rain':[32,176,'USA'],'Alex':[66,145,'广西']}
# 特性：

# 1、字典是可变，无序的数据集合(没有索引，因为可以通过key查询)
# 2、字典格式是key-value的数据类型,key是不可变的，key必须可以hash，value可变
# 3、查找速度快（是通过比二分法更快的方式进行查找的，通过hash函数将key转为数字，然后比较大小，进行查找）所以key必须可以hash
# 4、可存放任意多个值不唯一，

# 获取
print(dic1['jiangtao'])   #直接通过key获取
print(dic1.get('jiangtao'))  #通过get方法获取

# 修改
dic1['jiangtao'][0] = 27
print(dic1)
print(dic1['jiangtao'])
