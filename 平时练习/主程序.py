# ① import 包.模块之前的注释我都没删,我照着注释打一遍
import dongwuyuan

# ② from 包 import 模块
from dongwuyuan import 狗
from dongwuyuan import 猫


# ③ from 包.模块 import 工具
print(dongwuyuan.狗.狗叫())
print(dongwuyuan.猫.叫())
print(dongwuyuan.猫.抓老鼠())

# ④ import 包.模块 as 别名
import dongwuyuan.狗 as go
import dongwuyuan.猫 as mao



# ⑤ 验证包的身份
print(type(dongwuyuan))
print(dongwuyuan.__file__)#运行之后最后的结果看到的是init__.py,所以这是个包,不是模块

