# 字面量的写法
# print(100)#整数类型(int)
# print(3.1415)# 浮点数/小数(float)
# print(True)# 布尔
# print(False)#字符串
# print("hello world")#字符串
# print("----------")#字符串
# print(None)#空值
#
# # 布尔类型本质也是整数类型(Ture - 1; False - 0)
# print(True + 1)# 2
# print(False - 1)# -1

# 变量
# Python是动态类型语言,一个变量是可以存储不同类型数据的(但是项目开发中,推荐变量只存储一种类型的数据)
# num = 1114.1
# print(num)
#
# num = num + 1
# print(num)
#
# num = "OK"
# print(num)
#
# a = True
# print(a)

#  案例

# base = 20.7#  基础播放量
# incr = 50# 每一个月的新增播放量
# print("未来第一个月的播放总量:", base + incr)
# print("未来第二个月的播放总量:", base + incr + incr)

# 案例 - 升级 一次性可以定义多个变量
# 如下面所示,会分割开来
# base,incr = 20.7,50
# print("未来第一个月的播放总量:", base + incr)
# print("未来第二个月的播放总量:", base + incr + incr)
# # 定义的形式依旧还是   变量名 = 变量形式
# # 输出打印,参与计算,记录数据
# # 一条语句可以定义多个变量,也可以连续赋值(a,b = 1,2)

# 接下里尝试a值赋值给b,b给a
# 重新设置一个新的变量,新的容器(欸嘿,我自己想出来的)a = c b = c a = b
# 接下来就是尝试啦,视频我就先不看了
# a = 10
# b = 20
#
# c = a# c = 10
# a = b# a = 20
# b = c# b = 10 如果这时候再b = a 那b就= 20
#
# print(a,b)
# 这就是变量交换的办法
# 小练习 a = 1 b = 2 c = 3,令a = 3 b = 1 c = 2
a = 1
b = 2
c = 3

# u = a# u = 1
# a = c# a = 3
# c = b# c = 2
# b = u# c = 2
# print(a,b,c)

a, b, c = c, a, b

print(a, b, c) # 输出 3 1 2，直接搞定！
# 我想到的是一个一个来,逻辑倒推,但ai给的却是一起来,这个我确实没想到,直接用来当作参考了


