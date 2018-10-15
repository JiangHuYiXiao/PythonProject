#-*- coding:utf-8 -*-

L1 = [1,2,3,4,22,'jiangtao','jianghu','rose',1122,33,44]
# 1、列表最后元素后追加
L1.append(22)
print(L1[:])  #[1, 2, 3, 4, 22, 'jiangtao', 'jianghu', 'rose', 1122, 33, 44, 22]
# 2、增加列表元素
L1.insert(0,'增加')  #在索引值为0的位置增加一个元素
print(L1[:])

L1.insert(2,'XIU')  #在索引值为2位置增加一个元素
print(L1[:])

#3、修改列表元素
L1[0] = 2
print(L1[:]) #把索引0的元素‘增加’修改为2

#多个修改
L1 [0,1] = 1
print(L1[:])


