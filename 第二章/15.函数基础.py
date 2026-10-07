# 函数是组织好的，可重复使用的，用来实现特定
# 函数的定义
# 函数定义的时候并不会执行，只有在调用函数的时候，函数体的逻辑才会执行，函数必须先定义后调用
# cart = {}
# def run_cart_kt():
#     print("================")
#     print("    购物车列表    ")
#     print("增加购物车商品请按1")
#     print("修改购物车商品请按2")
#     print("删除购物车商品请按3")
#     print("查询购物车商品请按4")
#     print("退出购物车请按5")
#     i = int(input("请输入你想做的服务: "))
#     print("================")
#     return i  # 【核心修改】把 i 扔出去！
#
# def run_cart_tj():
# # 添加
#     name = input("请输入商品的名称: ")
#     jg = float(input("请输入商品的价格: "))
#     sl = float(input("请输入需要的商品的数量: "))
#     if name in cart:
#         print(f"{name}已存在购物车,请重新选择")
#     else:
#         cart[name] = {"价格": jg, "数量": sl}
#         print(f"商品{name}成功加入购物车")
#
# def run_cart_xg2():
#     name = input("请输入商品的名称: ")
#     if name not in cart:
#         print(f"对不起,{name}不存在购物车中")
#     else:
#         print("请选择你需要修改的部分,名称请按1,价格请按2,数量请按3,不需要请按0")
#         xg = int(input("请输入您要修改的数字: "))
#         if xg == 1:
#             new_name = input("请重新输入商品的名称: ")
#             cart[new_name] = cart.pop(name)
#             print("商品名称修改成功！")
#         elif xg == 2:
#             jg = float(input("请输入商品的价格: "))
#             cart[name]["价格"] = jg
#         elif xg == 3:
#             sl = float(input("请输入需要的商品的数量: "))
#             cart[name]["数量"] = sl
#
# def run_cart_sc3():
#     name = input("请输入您要删除的购物车中的物品: ")
#     if name in cart:
#         del cart[name]
#         print(f"购物车中的{name}去除成功")
#     else:
#         print(f"{name}不在购物车中")
#
# def run_cart_cx4():
#     for v, b in cart.items():
#         print(f"{v},{b}")
#
# def run_cart():
#     while True:
#         i = run_cart_kt()
#         if i == 1:
#             run_cart_tj()# 【核心修改】用变量 i 接住菜单函数返回出来的值
#         elif i == 2:
#             run_cart_xg2()
#         elif i == 3:
#             run_cart_sc3()
#         elif i == 4:
#             run_cart_cx4()
#         elif i == 5:
#             break
# # 调用函数
# run_cart()

# 如果返回值有多个，多个返回值之间逗号,分割.多个返回值会封装到元组当中
# round(数字,保留的小数位数)




