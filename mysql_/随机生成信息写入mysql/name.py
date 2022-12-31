# coding=utf-8
import random


# 常用汉字
def generate_name():
    surname = ["任", "李", "张", "赵", "王"]
    dict = ["爱", "婷", "聪", "通", "能", "侨"]
    # 打乱顺序
    random.shuffle(dict)
    font_string = ''
    # 随机调字符据并输出
    for i in range(0, random.randint(1, 2)):
        font_string += random.choice(dict)
    surname = random.choice(surname)
    return (surname + font_string)


if __name__ == '__main__':
    print(generate_name())
