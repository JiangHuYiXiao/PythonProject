#-*- coding:utf-8 -*-
dic1 = {'jiangtao':[18,170,'江西'],'jianghu':[34,190,'湖南'],'rain':[32,176,'USA'],'Alex':[66,145,'广西']}

# 1、判断：in
print('jianggong' in dic1) #False

# 2、查找：直接获取dic[] 或者通过get方法
print(dic1 ['jiangtao'])
# print(dic1 ['jiangtao1'])  #不存在时会报错

print(dic1.get('jiangtao'))
print(dic1.get('jiangtao1'))  #不存在时不报错，返回None

# 3、修改-增加： dic [] = 或者dic [] []
dic1 ['jiangtao'] = 'jiangjiang'  #这个是修改key：jiangtao的value值，为jiangjiang
# #注意：python中字典的键是不能直接修改，因为键是hash。
print(dic1)
dic1 ['jiangxifulao'] = ['jiangxifulao',22,'CHINA']
print(dic1)

# 但是可以间接修改key键值
dict = {'a': 1, 'b': 2}

dict["c"] = dict.pop("a")
print(dict)

# 4、删除
dic1.popitem()   #随机删除
print(dic1)

dic1.pop('jiangtao') #需要给定参数
print(dic1)

del dic1['jianghu']
print(dic1)
# 5、多级字典嵌套
dic3 = {'info':{'name':['jack','rose'],'age':{'teenage':[11,12,13,14]}}}

# 字典的其他方法
# 6、清空
dic3.clear()
print(dic3)

# 7、查询字典的key值
print(dic1)   #{'rain': [32, 176, 'USA'], 'Alex': [66, 145, '广西']}
print(dic1.keys()) #dict_keys(['rain', 'Alex'])

# 8、返回字典的value值
print(dic1.values())  #dict_values([[32, 176, 'USA'], [66, 145, '广西']])

# 9、把字典转换成列表
print(dic1.items())  #dict_items([('rain', [32, 176, 'USA']), ('Alex', [66, 145, '广西'])])

# 10、把两个字典进行合并
d1 = {1:23,2:24}
d2 = {'age':11,'sex':'female',1:[23,22,25]}
d1.update(d2) #把d2合并到d1上，如果d1有重复的key值时就更新value，没有重复的key时就将d2的key-value进行新增到d1中
print(d2)  #{'age': 11, 'sex': 'female', 1: [23, 22, 25]},不变

print(d1)   #{1: [23, 22, 25], 2: 24, 'age': 11, 'sex': 'female'}

# 11、setdefault有对应的key值则返回value，没有对应的key值则新增
d1.setdefault(1,333)
print(d1)    #{1: [23, 22, 25], 2: 24, 'age': 11, 'sex': 'female'}由于1这个key在原有字典是存在的所以不新增
d1.setdefault(11,333)
print(d1)   #{1: [23, 22, 25], 2: 24, 'age': 11, 'sex': 'female', 11: 333}由于11这个key在原有字典是不存在的所以新增
# 12、给定key后批量赋值
dic4 = dic1.fromkeys(['a','b','c'],1111)  #{'a': 1111, 'b': 1111, 'c': 1111}
print((dic4))

# 13、列表的循环
dic5 = {'jiangtao':[18,170,'江西'],'jianghu':[34,190,'湖南'],'rain':[32,176,'USA'],'Alex':[66,145,'广西']}
# 高效的循环：
for k in dic5:
    print(k)  #返回key

for k in dic5:  #通过key进行查询，本身我们字典的查询很快
    print(k,dic5[k])  #返回key和value

# 低效的循环
for k,v in dic5.items():   #通过将字典转换成列表再查找
    print(k,v)   #返回key和value