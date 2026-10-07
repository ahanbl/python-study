# a = 1# int
# 如果想查看比如a = ? 数据太乱太杂不知道,可以通过type()语句来查看,记得在前面输出
# print(type(a))
# type是查看类型?我待会看看,是查看变量里面数据的类型,比如占位符什么乱七八糟的
# class 表示类型,class 后面表示的就是你输出物品的类型
# 获取数据的类型,比如bool int None float
# 变量本身没有类型,只能查看变量里数据的类型
# 以上就是type工具
from socketserver import BaseRequestHandler

# 如果想查看比如a = 什么数据 数据太乱太杂不知道,可以通过isinstance()语句来查看,记得在前面输出
# 这个语句输出的是bool值,例如True False ,用来判断自己检查的变量,数据是不是指定的类型
# print(isinstance(a, int))# True
# print(isinstance(a, bool))# False
# print(isinstance(a, float))# False

# 接下来就是字符串 双引号，单引号，三引号（多行字符串）
# 字符串
# 三种方式
# s1 = "Hello" # 双引号定义 都不支持换行
# s2 = 'Python' # 单引号定义
# s3 = """
# Hello:
#     阿涵今天也很棒哦
#     今天也开始学了,真棒
# """# 三引号定义(多行字符串)
# print(s1, s2, s3)
# print(type(s1), type(s2), type(s3))

# 定义字符串 ---→ It's very good
# 会发现如果令 msg = 'It's...之后,会直接将It定为定义
# 这时候就需要用到字符串中的转译字符
# 转译字符就是\,只要在字符前加上\(\',\"就可以)让他表示本身
# \n表换行 \t表缩进(tab空行的效果)
# msg = 'it\'s very good'# \'会红是正常的
# print(msg)
#
# msg2 = "\t欲穷千里目\n\t更上一层楼"
# print(msg2)

# 字符串的拼接 --->只能拼接字符串,不能拼接int(数字类型!)如果想拼接需要str(int数字)这串代码转字符串
# 接下来开始案例
# name = "ahan"
# age = 20
# pro = "电气"
# hobby = "Python,Java"
#
# print("大家好" + ",我是" + name + "," + "今年" + str(age) + "岁" + "," + "学习的专业是" + pro + "," + "爱好" + hobby)
# 注意,字符串的拼接就是字面意思,只能拼接字符串而不能拼接数字int等
# 拼接繁琐,破坏字符串完整性,类型转换
# 使用+号拼接还是太繁琐了,有没有更简单的办法
# 有的兄弟,有的,字符串格式化了解一下


# 占位符(%s),前面有多少占位符(%s),后面就需要有多少个变量(或数据),前后数量要保持一致
# # 字符串格式化 第一种方式 ---> %s占位符
# name = "ahan"
# age = 20
# pro = "电气"
# hobby = "Python,Java"
#
# print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好%s" %(name, age, pro, hobby))

# 兄弟兄弟,这个还是太麻烦了,有没有更方便更快捷的办法来快速加入
# 有的兄弟,有的
# 字符串格式化 第二种方式 ---> f"...{变量名/表达式}..." ---->推荐方式
name = "ahan"
age = 20
pro = "电气"
hobby = "Python,Java"

print(f"大家好,我是 {name} ,今年 {age} 岁,学习的专业是 {pro} ,爱好 {hobby}" )
# input print
