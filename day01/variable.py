# -*- coding:utf-8 -*-

# 一、变量的定义：
# 1、变量名只能是数字、字母、数字、下划线组成的任意集合
# 2、变量名的第一个字符不能是数字
# 3、不能使用python的关键字（and,or,if,while,print,continue,break等。）
# 4、变量的命名应该具有见名思意，不能拼音。
# 5、尽量格式为下划线的形式如：old_body,(建议)，OldBody（不建议）
#比如：
name = 2
name2 = 3
name_3 = 4
#name-e=2 中横线不能，因为他是减号
# 21name = 55 数字不能再开头

# 二、变量的作用：所谓变量就是把程序运行中间的值存储到变量中，以便后面的程序调用。

# 三、变量的引用
print(name)
print(name + name2)
# 重新赋值
name = 7
print(name)

# 注意：
# 变量赋值本质是改变变量所在内存地址的值。
# 比如：
a = 1
b = a #把b的值赋给a，实质是让a重新指向b所在的内存地址。
print(a) #1
print(b) #1

a = 6

print(a) #6
print(b) #1 因为b所指向的内存地址未发生改变所以还是1
