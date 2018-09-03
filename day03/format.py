#-*- coding:utf-8 -*-
# 格式化输出主要是为了按照一定的格式输出数据。
# 针对于字符串，一般用%s进行占位，它可以满足字符串、数字、小数。
# 也可以用%d进行占位代表数字。
# %f占位代表小数。
#input()方法会把所有的输入都转换为字符串

# 需求：按照下面这个格式输出结果

# ----------info of 刘邦---------
# 名字：刘邦
# 年龄：28
# 工作：皇帝
# 家乡：汉朝
# ------------end----------------

# 定义变量
name = input('名字：')
age = input('年龄：')
#或者使用%d进行占位，但是要使用int（）方法进行转换，因为input方法的输出为字符串，需要进行转换。
# age = int（input('年龄：')）
job = input('工作：')
hometown = input('家乡：')

info = '''
----------info of %s---------
名字： %s
年龄： %s
工作： %s
家乡： %s
------------end-----------------
''' %(name,name,age,job,hometown)
# 输出
print(info)

# 定义变量
name1 = input('名字：')
age1 = int(input('年龄：'))
job1 = input('工作：')
hometown1 = input('家乡：')

info1 = '''
----------info of %s---------
名字： %s
年龄： %d
工作： %s
家乡： %s
------------end-----------------
''' %(name1,name1,age1,job1,hometown1)
# 输出
print(info1)