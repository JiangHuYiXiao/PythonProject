#-*- coding:utf-8 -*-
# 写一个循环不断的问用户想买什么，用户选择一个编号，就把对应的商品加到购物车里面，最终用户输入q时，退出，打印购物车里面的商品列表。
products = [['Iphone8',6888],['MacPro',14800],['小米6',2499],['coffe',31],['Book',80],['Nike shoes',799]]
while True:
    for index,i in enumerate(products):
        print( index,i)
    choice = (input("请输入商品编号："))
    shopping_cart = []
    if choice.isdigit():
        choice = int(choice)
        if choice >=0 and choice <= len(products) :
            shopping_cart.append(products[choice])
            print(shopping_cart[:])
    elif choice == 'q':
            break
    else:
        print("你输入的商品不存在")
