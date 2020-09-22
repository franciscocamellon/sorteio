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


class Chicken_Dinner():

    def __init__(self):
        """
        Class constructor.
        """
        # self.students = students
        self.order = []

    def chicken_dinner(self):
        """
        This function randomly shuffle the student's list.
        """
        st_list = self.students_list()
        while len(st_list) > 0:
            random.shuffle(st_list)
            self.order.append(st_list.pop(0))
        return self.order

    def students_list(self):
        formated_list = []
        file = open('students2.txt', 'r', encoding="utf8")
        for line in file:
            n_line = line.replace('\n', '')
            formated_list.append(n_line)
            formated_list.sort()
        return formated_list

    def print_result(self):
        """
        This function prints the order
        """
        a = self.chicken_dinner()
        print('===' * 21,
              '{:^63}'.format('Sorteio'),
              '===' * 21, '  A ordem de apresentação é: \n',
              '  Prioridades: \n', sep="\n")
        print('---' * 21,
              '  Vala comum: \n', sep="\n")

        for i in range(len(a)):
            print('    {}º - {}'.format(i+1, a[i]))

        print('---' * 21,
              '{:>63}'.format('Autor: Francisco Camello'), sep="\n")


# students = ['Joao', 'Maria', 'Jose', 'Joaquim', 'Madalena', 'Enyel']
Chicken_Dinner().print_result()
