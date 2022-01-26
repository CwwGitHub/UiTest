from enum import Enum

# 创建枚举
class Color(Enum):
    RED = 1
    BLACK =2

# 获取枚举成员的name和value
print(Color.RED.name)
print(Color.RED.value)