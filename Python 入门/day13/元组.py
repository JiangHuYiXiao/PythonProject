#-*- coding:utf-8 -*-
# 元组：也是一个数据的集合，也是有序的，但是它不可变，也称作为只读列表，用小括号()

# 特性：元组本身不可变，但是里面可以包含列表，所以元组间接也是可变的。
# 元组功能：index，count，切片
tuple1 = (1,334,343,'fds',1,2222,1)

# tuple1.index()获取索引值
print(tuple1.index(334)) #1

# tuple1.count() 统计数据量
print(tuple1.count(1)) #3
# 使用场景：
# 显示的告诉别人此处的数据不可修改。比如配置信息




