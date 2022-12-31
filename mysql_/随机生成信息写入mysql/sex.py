import random


def generate_sex():
    sex = None
    sex_id = random.randrange(0, 2)
    if sex_id == 0:
        sex = '男'
    else:
        sex = '女'

    return sex


if __name__ == '__main__':
    print(generate_sex())
