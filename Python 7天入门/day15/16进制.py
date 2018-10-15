#-*- coding:utf-8 -*-
# 为何要使16进制

# 1、
# 计算机硬件是0101的二进制，16进制刚好是2的倍数，更容易表达一个命令或者数据，
# 十六进制更加简短，因为换算的时候一个十六进制可以代替4个二进制数也就是8位（8进制可以代替三个二进制），也就是一个字节。
# 1 字节 = 8位(1byte = 8bit)
# 1 字 = 2字节(1word = 2byte)

# 2、
# 最早规定ASCII码的采用的就是8bit（后期由于中文等的扩展，但基础单位还是8bit），
# 8bit用两个16进制就可以表达出来，用二进制要四个可以表达出来，不管是阅读还是存储都比其他进制要方便。

# 3、
# 计算机中的CPU运算也是遵循ASCII字符集，以16,32,64这样的方式在发展，因此数据交换时使用16进制也显得更好。

# 4、为了统一规范，CPU,内存，硬盘都是16进制计算

# 也就是说与传输速度有关的b一般指的是bit。与容量有关的b一般指的是byte。

# 虽然二进制有不少优点,但毕竟我们日常生活中用的都是十进制,为了能通用,就有必要把它转换为十进制.至于为什么用八进制和十六进制呢?
# 很简单,就是因为它是2的乘方,2(3)=8,2(4)=16,这样一来就便于二进制的计算和阅读.
# 对于其它进制转换为十进制比较简单,下面举例说明:在此说明一下,一般常用进制有简写,
# 这样是为了不混淆,如十进制一般在末尾加个字母D[一般习惯都不加],二进制加个B,八进制Q,十六进制H.

# 例如
# 1、各种进制转换为10进制
# :123D、1101B、123Q、AB9H
# 123D=1×10^2+2×10^1+3×10^0=123 0.11D=1*10(-1)+1*10(-2)
# 1011B=（1×2^3+0×2^2+1×2^1+1×2^0）D=11 0.11B=1*2(-1)+1*(-2)
# 123Q=（1×8^2+2×8^1+3×8^0）D=83 0.11Q=1*8(-1)+1*8(-2)
# AB9H=（10×16^2+11×16^1+9×16^0）D=2745 0.11H=1*16(-1)+1*16(-2)

# 2、10进制转换为各种进制
# 85转换为2进制，8进制，16进制
print(bin(85))  #0b1010101 二进制
print(hex(85))  #0x55  16进制
print(oct(85))  #0o125  8进制

# python中各种进制转换函数

# 	      2进制	           8进制	                 10进制   	         16进制
# 2进制	   -	         bin(int(x, 8))   	bin(int(x, 10)) 	bin(int(x, 16))
# 8进制  oct(int(x, 2))	    -	            oct(int(x, 10))	    oct(int(x, 16))
# 10进制	 int(x, 2)	     int(x, 8)	              -	            int(x, 16)
# 16进制 hex(int(x, 2))   hex(int(x, 8))    	hex(int(x, 10))     	-
# 16进制转二进制
print(bin(int(0x58)))  #0b1011000

# 二进制转16进制

print(hex(int(0b1011000))) #0x58
