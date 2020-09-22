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
        # self.students = students
        self.order = []

    def students_list(self):
        common, second_day, prio_first_day, prio_second_day = [], [], [], []

        with open('students2.txt', 'r', encoding="utf8") as jsonFile:
            st_dict = json.load(jsonFile)

        for k, v in st_dict.items():
            if v == 0 or v == 1:
                prio_first_day.append(k)
            elif v == 5:
                common.append(k)
            elif v == 2 or v == 3:
                prio_second_day.append(k)
            else:
                second_day.append(k)
        return common, prio_first_day, prio_second_day

    def common(self):
        """
        This function randomly shuffle the student's list.
        """
        common = self.students_list()[0]
        common_order, common_order_23, common_order_30 = [], [], []

        while len(common) > 0:
            random.shuffle(common)
            common_order.append(common.pop(0))
        half = len(common_order)//2
        common_order_23 = common_order[:half]
        common_order_30 = common_order[half:]

        return common_order_23, common_order_30

    def prio_first_day(self):
        """
        This function randomly shuffle the student's list.
        """
        prio_first_day = self.students_list()[1]
        prio_first_day_order = []

        while len(prio_first_day) > 0:
            random.shuffle(prio_first_day)
            prio_first_day_order.append(prio_first_day.pop(0))
        return prio_first_day_order

    def prio_second_day(self):
        """
        This function randomly shuffle the student's list.
        """
        prio_second_day = self.students_list()[2]
        prio_second_day_order = []

        while len(prio_second_day) > 0:
            random.shuffle(prio_second_day)
            prio_second_day_order.append(prio_second_day.pop(0))
        return prio_second_day_order

    def print_result(self):
        """
        This function prints the order
        """
        pf_day, ps_day = self.prio_first_day(), self.prio_second_day()
        f_day, s_day = self.common()[0], self.common()[1]

        print('===' * 21,
              '{:^63}'.format('Sorteio'),
              '===' * 21, '  A ordem de apresentação é: \n',
              '  Prioridades do primeiro dia: \n', sep="\n")
        for i in range(len(pf_day)):
            print('    {}º - {}'.format(i+1, pf_day[i]))

        print('---' * 21,
              '  Vala comum do primeiro dia: \n', sep="\n")

        for i in range(len(f_day)):
            print('    {}º - {}'.format(i+4, f_day[i]))

        print('---' * 21,
              '  Prioridades do segundo dia: \n', sep="\n")
        for i in range(len(ps_day)):
            print('    {}º - {}'.format(i+1, ps_day[i]))

        print('---' * 21,
              '  Vala comum do segundo dia: \n', sep="\n")
        for i in range(len(s_day)):
            print('    {}º - {}'.format(i+5, s_day[i]))

        print('---' * 21,
              '{:>63}'.format('Autor: Francisco Camello'), sep="\n")


# students = ['Joao', 'Maria', 'Jose', 'Joaquim', 'Madalena', 'Enyel']
Chicken_Dinner().print_result()
