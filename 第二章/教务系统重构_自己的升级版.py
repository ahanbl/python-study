# 教务系统的重新开发,我自己来
# 1 添加学生成绩:根据输入的学生姓名,语文成绩,数学成绩,英语成绩,记录在系统中
# 我觉得,这里的话这些我都可以做成一个一个的函数来,然后全部整合成一个类
class Student:
    subject1 = ["语文", "数学", "英语", "物理", "化学", "生物", "历史", "政治", "地理"]
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def lr_score(self, subject, score):
        # self.subject = subject
        # self.score = score 这两行完全没必要,都多余了
        if subject in self.subject1:
            self.scores[subject] = score
        if subject not in self.subject1:
            raise ValueError(...)  # ← 用 raise，不是 return,这里的代码我先复制下来

    def __str__(self):
        mx = ""
        for km, fs in self.scores.items():# 从字典中拉出km,fs
            mx = mx + f"{km}{fs}"# mx = mx?这是什么
        return f"{self.name}: {mx}"



# 接下来的功能就都是教务系统该做的了,面向学生的功能已经做完了
# 2 修改学生成绩: 根据输入的学生姓名,修改对应的学生成绩
class JiaoWuSystem:
    def __init__(self):
        self.all_student = {}
# 1 and 2 录入 和 修改 一起进行     问姓名，判断重名，造一个学生，放进容器
    def lr_JiaoWuSystem(self):
        name = input("请输入要录入或是要修改的学生姓名: ")
        subject, score = input("请输入要修改的科目以及分数(空格隔开): ").split()
        if name in self.all_student:
            # 交给【那个学生自己】改
            #这一段的输入成绩直接关掉就行了,难怪后面的subject一直报错
            # 这一段是直接用学生类的录入来修改成绩的吧
            # 让学生自己改,也就是用教务处的学生让教务处里的学生自己改,而不是前面的面向学生的类,再套面向学生的方法
        #     "这个方法，是【我（self）】会做的，还是【别人（self.某个东西）】会做的？"  点号左边的东西，必须"真的有"右边那个方法。
        else:
            new_student = Student(name)
            # 忘记了这个是新学生,直接复制粘贴上面的了

        self.all_student[name].lr_score(subject, int(score))
    def cflr_JiaoWuSystem(self):
        while True:
            print("需要请按1,不需要请按2")
            i = int(input("你是否还需要修改学生档案: "))
            if i == 1:
                self.lr_JiaoWuSystem()
            elif i == 2:
                break
            else:
                print("输入错误,请重新输入")





# 3 删除学生成绩: 根据输入的学生姓名,删除对应的学生成绩




# 4 查询指定学生成绩: 根据输入的学生姓名,查找对应的学生成绩,并输出




# 5 展示全部学生成绩: 展示出系统中所有学生的成绩