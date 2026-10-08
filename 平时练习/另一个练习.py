# 1 导入我练习中的函数
# from 练习 import 敲钉子
# print(敲钉子())# 完全没必要f"{}",直接输出就行了,我还是老毛病了
# import 练习
# print(练习.量长度(1))# 错误点,我在import 练习之后,直接输出量长度发现不行,必须得练习.量长度才可以
# print(练习.锤子)
# import 练习 as n6
# print(n6.锤子)

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f'{self.name}, {self.score}'
s1 = Student("小明","语文:80")
print(s1)