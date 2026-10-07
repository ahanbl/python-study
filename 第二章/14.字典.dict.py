# Python中的字典(dict)，里面存储的是键值对(key: value)类型的数据，可以根据键(key)找到对应的值(value)。
# 特点:键值对(key:value)存储、键(key) 不能重复 、可修改。
# 字典（dict）中的value可以是任何类型的数据，但key不能为可变类型（如list， set， dict）等
# key重复了， 后面的值会覆盖前面的值
# 访问字典 print（dict1['1']）
# 修改字典 dict1["1"] = 666
# 字典 dict 是没有独立下标,不可索引
from getopt import gnu_getopt

# 字典 dict 的方法
#  增
# 字典名称[key]=value   往指定字典中添加key-value键值对    dict1["涛哥"] = 688
#  删
# 字典名称.pop(key)     删除字典中指定的key，并返回该key对应的value score = dictl.pop("涛哥")
# del 字典名称[key]     删除字典中指定的键值对（不返回删除的值）     del dicti["涛哥"]
#  改
# 字典名称[key]=value       修改字典中指定的key对应的值     dict1["小智"]=658
#  查
# 字典名称[key]     根据key获取value    dict1["涛哥"]
# 字典名称.get(key) 根据key获取value    dictl.get("涛哥")
# 字典名称.keys()   获取所有的key    dictl.keys()
# 字典名称.values() 获取所有的value  dictl.values()
# 字典名称.items()  获取所有的key-value键值对   dictl.items()

# 案例 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据
# 通过控制台菜单与用户交互。具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
# 5.退出购物车

# # 1 先输入名称,数量,价格,然后再问需不需要修改,具体修改什么?,我觉得太简单了,单个商品的话太少了,我直接多个商品,然后做一个字典
# cart = {}
# while True:
#     name = input("请输入商品的名称: ")
#     jg = input("请输入商品的价格: ")
#     sl = input("请输入需要的商品的数量: ")
#     while True:
#         print("请选择你需要修改的部分,名称请按1,价格请按2,数量请按3,不需要请按0")
#         xg = int(input("请输入您要修改的数字: "))
#         if xg == 1:
#             name = input("请重新输入商品的名称: ")
#         elif xg == 2:
#             jg = input("请输入商品的价格: ")
#         elif xg == 3:
#             sl = input("请输入需要的商品的数量: ")
#         if xg == 0:
#             break
#     while True:
#         print("你是否需要增加购物车中的物品,需要请按1,不需要请按2")
#         zj = int(input("请输入1或2: "))
#         if zj == 2:
#             cart[name] = {"价格": jg, "数量": sl}
#
#         break
#     if zj == 1:
#         cart[name] = {"价格": jg, "数量": sl}
#         continue
# # 3 是否需要删除
#     while True:
#         print("你是否需要删除购物车中的物品,需要请按1,不需要请按2")
#         sc = int(input("请输入你的数字: "))
#         if sc == 1:
#             name = input("请输入您要删除的购物车中的物品: ")
#             for name in cart:
#                 del cart[name]
#                 print(f"购物车中的{name}去除成功")
#                 break
#             else:
#                 print("购物车中并没有你输入的物品")
#                 break
#         break
#     break
# # 最后输出购物车,查询
# for k,v in cart.items():
#     print(k,v)

# cart = {}
# while True:
#    print("================")
#    print("    购物车列表    ")
#    print("增加购物车商品请按1")
#    print("修改购物车商品请按2")
#    print("删除购物车商品请按3")
#    print("查询购物车商品请按4")
#    print("退出购物车请按5")
#    i = int(input("请输入你想做的服务: "))
#    print("================")
#    # 添加
#    if i == 1:
#        name = input("请输入商品的名称: ")
#        jg = float(input("请输入商品的价格: "))
#        sl = float(input("请输入需要的商品的数量: "))
#        if name in cart:
#            print(f"{name}已存在购物车,请重新选择")
#        else:
#            cart[name] = {"价格": jg, "数量": sl}
#            print(f"商品{name}成功加入购物车")
#    # 修改
#    elif i == 2:
#        name = input("请输入商品的名称: ")
#        if name not in cart:
#            print(f"对不起,{name}不存在购物车中")
#        else:
#            print("请选择你需要修改的部分,名称请按1,价格请按2,数量请按3,不需要请按0")
#            xg = int(input("请输入您要修改的数字: "))
#            if xg == 1:
#                new_name = input("请重新输入商品的名称: ")
#                cart[new_name] = cart.pop(name)
#                print("商品名称修改成功！")
#            elif xg == 2:
#                jg = float(input("请输入商品的价格: "))
#                cart[name]["价格"] = jg
#            elif xg == 3:
#                sl = float(input("请输入需要的商品的数量: "))
#                cart[name]["数量"] = sl
#
#    # 删除
#    elif i == 3:
#        name = input("请输入您要删除的购物车中的物品: ")
#        if name in cart:
#            del cart[name]
#            print(f"购物车中的{name}去除成功")
#        else:
#            print(f"{name}不在购物车中")
#    # 查询
#    elif i == 4:
#        for v, b in cart.items():
#            print(f"{v},{b}")
#    elif i == 5:
#        break
#    else:
#        print("非法操作,不支持")


# 1.添加学生信息：根据提示录入学生姓名，语文，数学，英语成绩，录入完成保存到系统中
cj = {}
gn = """
按1添加
按2修改
3删除
4查询
5列出成绩
6统计max,min三科的人和分手
7退出
"""
while True:
    print(gn)
    i = int(input("功能: "))
    if i == 1:
        name = input("请输入同学的姓名: ")
        yw, sx, yy = map(float,input("语文,数学,英语,空格隔开: ").split())
        cj[name] = {"语文": yw, "数学": sx, "英语": yy}
    if i == 2:#这个我就不弄什么分开修改分数啥的了,随笔写了
        name = input("请输入同学的姓名: ")
        yw, sx, yy = map(float,input("语文,数学,英语,空格隔开: ").split())
        if name not in cj:
            print(f"{name}不存在")
        else:
            cj[name] = {"语文": yw, "数学": sx, "英语": yy}
    if i == 3:
        name = input("请输入删除的同学的姓名: ")
        if name not in cj:
            print("不存在")
        else:
            del cj[name]
            print("成功")
    if i == 4:
        name = input("请输入查找的同学的姓名: ")
        if name not in cj:
            print("不存在")
        else:
            cx = cj[name]
            print("cx")
    if i == 5:
        for v, b in cj.items():
            print(v, b)
    if i == 6:# 按照ds说的比武招亲式,我没记下太多代码,我试试看自己写,一个一个遍历出来我想想,字典的形式
        max_yw, min_yw = 0, 100
        max_sx, min_sx = 0, 100
        max_yy, min_yy = 0, 100
        max_name, min_name = "", ""
        for k, v in cj.items():
            # 先写语文的max and min
            v1 = v["语文"]
            if v1 > max_yw:
                max_yw = v1
                max_name = k
            if v1 < min_yw:
                min_yw = v1
                min_name = k
            # 输出
        print(f"{max_name},{max_yw}")
    if i == 7:
        break



































