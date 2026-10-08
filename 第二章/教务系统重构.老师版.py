# 教务系统的重新开发,我自己来
# 1 添加学生成绩:根据输入的学生姓名,语文成绩,数学成绩,英语成绩,记录在系统中
# 我觉得,这里的话这些我都可以做成一个一个的函数来,然后全部整合成一个类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f'{self.name} :丨语文:{self.chinese}丨 数学{self.math} 丨 英语{self.english} 丨 总分{self.english + self.chinese + self.math} 丨'

# 2 修改学生成绩: 根据输入的学生姓名,修改对应的学生成绩
    def update_score(self, chinese = None, math = None, english = None):
        if self.chinese is not None:
            self.chinese = chinese
        if self.math is not None:
            self.math = math
        if self.english is not None:
            self.english = english




# 3 删除学生成绩: 根据输入的学生姓名,删除对应的学生成绩



# 4 查询指定学生成绩: 根据输入的学生姓名,查找对应的学生成绩,并输出



# 5 展示全部学生成绩: 展示出系统中所有学生的成绩



