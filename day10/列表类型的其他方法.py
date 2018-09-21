#-*- coding:utf-8 -*-

L1 = [1,2,33,444,33,'佩奇','jack','jiangtao',23,24,454,777,999,100,111,112]
print('------一、 列表删除------')
# 删除最后的元素
print(L1.pop())    #112

# 删除元素L1.remove（元素）
L1.remove('佩奇')   #[1, 2, 33, 444, 33,'jack', 'jiangtao', 23, 24, 454, 777, 999, 100, 111]
print(L1[:])

L1.remove(33)   #删除第一次出现的元素33，remove只支持一个个删除，
print(L1[:])

del L1[2]       #删除指定索引值对应的元素，
# del是python中的一个全局变量，可以删除python中的所有对象，
# L1.指的是L1这个变量调用某个方法
print(L1[:])
# del支持批量删除
del L1[0:3]  #删除0,1,2三个索引对应的元素
print(L1[:])


print('------二、列表循环------')
# 循环格式：for i in L1
#    print（i）
for i in L1:
    print(i)

print('----------------')
for i in range(10):
    print(i)
# while 和for循环的区别是，while循环可以不存在边界，存在死循环
# for 不存在死循环，一定是存在边界

print('--------三、排序-------')
L2 = [1,2,3243,55,66,879,322,'jiangtao','龙','蛇']  #这个不支持排序，int和str
L2.remove('jiangtao')
L2.remove('龙')
L2.remove('蛇')
print(L2[:])
L2.sort()
print(L2[:])

L3 = ['a','bc','gg','tt','b','AA']
L3.sort()   #['AA', 'a', 'b', 'bc', 'gg', 'tt']
print(L3[:])

L3.insert(2,'#')
print(L3[:])
L3.insert(2,'@')
L3.insert(2,'*')
print(L3[:])
L3.sort()
print(L3[:])   #排序结果是按照ASCII码表顺序排序的，['#', '*', '@', 'AA', 'a', 'b', 'bc', 'gg', 'tt']

print('-------倒序-------')
L3.reverse()
print(L3[:])


print('-------列表拼接--------')
L4 = [1,2,4]
#方法1
L5 =(L3 + L4)
print(L5[:])    #['tt', 'gg', 'bc', 'b', 'a', 'AA', '@', '*', '#', 1, 2, 4]
#方法2

L6 = [12,3432,434,'REWRE']
L7 = ['a','ff','12']
L6.extend(L7)
print(L6[:])

print('-------列表清空--------')
L8 = [11,22,33]
L8.clear()
print(L8[:])
List1 = [1,2,4]
List2 = List1.copy()
print(List2[:])

# 列表的赋值值是否改变
N1 = [12,13,14]
N2 = N1
print(N2[:])
N2[2] = 15
print(N2[:])
print(N1[:])
#两个列表的元素都改变了，
#如果修改了其中一个元素的值，另一个的也会改，不像我们的基本类型，改了其中一个另一个是不会改的

# 列表这种情况可以使用copy进行解决
N3 = N1.copy()
print(N3[:])
N1[1] = 222
print(N3[:])
print(N1[:])


# a = 12
# b = a
# print(a,b)
# b = 13
# print(a,b)   #不像我们的基本类型，改了其中一个另一个是不会改的

