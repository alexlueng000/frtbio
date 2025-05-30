# utils.py 各种工具函数
import random


# 生成3个5-60之间的随机数
def generate_random_number() -> list[int]:
    return [random.randint(5, 60) for _ in range(3)]