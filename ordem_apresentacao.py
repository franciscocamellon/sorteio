# -*- coding: utf-8 -*-
"""
/***************************************************************************
*    Algoritmo para sortear a ordem de apresentação da disciplina Projeto  *
* de Bloco                                                                 *
*        Aluno: Francisco Alves Camello Neto                               *
*                                                                          *
***************************************************************************/
"""

import random
import json


class Chicken_Dinner():

    def __init__(self):
        """
        Class constructor.
        """
        #self.common = list

    def students_list(self):
        """
        This function filter the students from your priority
        level from a students_dict.
        """

        common, zero, one, two, three = [], [], [], [], []

        with open('students2.json', 'r', encoding="utf8") as jsonFile:
            st_dict = json.load(jsonFile)

        for k, v in st_dict.items():
            if v == 0:
                zero.append(k)
            elif v == 1:
                one.append(k)
            elif v == 2:
                two.append(k)
            elif v == 3:
                three.append(k)
            else:
                common.append(k)

        return common, zero, one, two, three

    def no_priority(self):
        """
        This function randomly shuffle the student's in 
        the no priority list and divide between first and second day.
        """
        common = self.students_list()[0]
        common_order, common_order_23, common_order_30 = [], [], []

        while len(common) > 0:
            random.shuffle(common)
            common_order.append(common.pop(0))
        half = len(common_order)//2
        another_half = len(common_order)-half
        common_order_23 = common_order[:half]
        common_order_30 = common_order[another_half:]

        return common_order_23, common_order_30

    def prio_zero(self):
        """
        This function randomly shuffle the student's in 
        the priority list for the first day.
        """

        prio_zero = self.students_list()[1]
        prio_one = self.students_list()[2]
        prio_zero_ordered = []

        while len(prio_zero) > 0:
            random.shuffle(prio_zero)
            prio_zero_ordered.append(prio_zero.pop(0))
        while len(prio_one) > 0:
            random.shuffle(prio_one)
            prio_zero_ordered.append(prio_one.pop(0))
        return prio_zero_ordered

    def prio_two(self):
        """
        This function randomly shuffle the student's in 
        the priority list for the second day.
        """

        prio_two = self.students_list()[3]
        prio_three = self.students_list()[4]
        prio_two_order = []

        while len(prio_two) > 0:
            random.shuffle(prio_two)
            prio_two_order.append(prio_two.pop(0))
        while len(prio_three) > 0:
            random.shuffle(prio_three)
            prio_two_order.append(prio_three.pop(0))
        return prio_two_order

    def print_result(self):
        """
        This function prints the order
        """

        pf_day, ps_day = self.prio_zero(), self.prio_two()
        f_day, s_day = self.no_priority()[0], self.no_priority()[1]
        count1, count2 = len(pf_day), len(ps_day)

        print('  Prioridades do primeiro dia: \n')
        for i in range(len(pf_day)):
            print('    {}º - {}'.format(i+1, pf_day[i]))

        print('---' * 21,
              '  Vala comum do primeiro dia: \n', sep="\n")

        for i in range(len(f_day)):
            print('    {}º - {}'.format(count1+1, f_day[i]))
            count1 += 1

        print('---' * 21,
              '  Prioridades do segundo dia: \n', sep="\n")
        for i in range(len(ps_day)):
            print('    {}º - {}'.format(i+1, ps_day[i]))

        print('---' * 21,
              '  Vala comum do segundo dia: \n', sep="\n")
        for i in range(len(s_day)):
            print('    {}º - {}'.format(count2+1, s_day[i]))
            count2 += 1


print('===' * 21, '{:^63}'.format('Sorteio'), '===' *
      21, '  A ordem de apresentação é: \n', sep="\n")

Chicken_Dinner().print_result()

print('---' * 21,
      '{:>63}'.format('Autor: Francisco Camello'), sep="\n")
