self.subject = subject
            self.score = score
if subject not in self.subject1:
    # return f"{subject}这门科目不存在"这一行我先注释掉,复制报错的
    raise ValueError(f"{subject} 这门科目不存在")

if subject not in self.subject1:
    # return f"{subject}这门科目不存在"这一行我先注释掉,复制报错的
    raise ValueError(f"{subject} 这门科目不存在")

if __name__ == "__main__":
    s1 = Student("小明")
    s1.lr_score("语文", 80)
    print(s1)
    def