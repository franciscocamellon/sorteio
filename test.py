import random
import json


def students_list():
    common, second_day, prio_first_day, prio_second_day = [], [], [], []

    with open('students2.txt', 'r', encoding="utf8") as jsonFile:
        st_dict = json.load(jsonFile)

    for k, v in st_dict.items():
        if v == 0:
            prio_first_day.append(k)
        elif v == 1:
            common.append(k)
        elif v == 2:
            prio_second_day.append(k)
        else:
            second_day.append(k)
    return common, prio_first_day, prio_second_day


def common():
    """
    This function randomly shuffle the student's list.
    """
    common = students_list()[0]
    common_order, common_order_23, common_order_30 = [], [], []

    while len(common) > 0:
        random.shuffle(common)
        common_order.append(common.pop(0))
    half = len(common_order)//2
    common_order_23 = common_order[:half]
    common_order_30 = common_order[half:]

    return print(common_order_23, common_order_30, sep=' \n')
    
def prio_first_day():
    """
    This function randomly shuffle the student's list.
    """
    prio_first_day = students_list()[1]
    prio_first_day_order = []

    while len(prio_first_day) > 0:
        random.shuffle(prio_first_day)
        prio_first_day_order.append(prio_first_day.pop(0))
    return print(prio_first_day_order)
    
def prio_second_day():
    """
    This function randomly shuffle the student's list.
    """
    prio_second_day = students_list()[2]
    prio_second_day_order = []

    while len(prio_second_day) > 0:
        random.shuffle(prio_second_day)
        prio_second_day_order.append(prio_second_day.pop(0))
    return print(prio_second_day_order)


common()
