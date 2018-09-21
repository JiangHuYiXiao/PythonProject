#-*- coding:utf-8 -*-

# 1、创建一个列表names，
names = ['jack','rain','mack','racheal','shanshan']

# 2、往names列表里面的jack前面插入一个alex
names.insert(0,'alex')
print(names[:])

# 3、把shanshan元素改成中文
names[-1] = '姗姗'
print(names[:])

# 4、往names里面的rain后面插入一个子列表[oldboy,oldgirl]
a = (names.index('rain'))  #rain的索引值为2
old = ['oldboy','oldgirl']
# 在指定索引地方进行添加只能通过insert方法进行添加
names.insert(2,old)
print(names[:])
# 列表尾部增加
names.append(old)
print(names[:])

# 或者另外一种方法‘拼接’
names.extend(old)
print(names[:])
# 5、返回racheal的索引值

print(names.index('racheal'))

# 6、创建新列表L1 = [1,2,3,4,5,6]合并到names中
L1 = [1,2,3,4,5,6]
names.extend(L1)
print(names[:])
# 7、取出names列表中的索引6-10的元素
print(names[6:10])
# 8、取出索引[2,10]的值，并且步长为2
print(names[2:10:2])
# 9、取出列表的最后三个元素
print(names[-4:-1])  #只能从左到右进行取数