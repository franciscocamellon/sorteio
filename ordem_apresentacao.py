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

    def __init__(self, students):
        """
        Class constructor.
        """
        self.students = students
        self.order = []

    def chicken_dinner(self):
        """
        This function randomly shuffle the student's list.
        """
        while len(students) > 0:
            random.shuffle(students)
            self.order.append(students.pop(0))
        return self.order

    def print_result(self):
        """
        This function prints the order
        """
        a = self.chicken_dinner()
        print('===' * 21,
              '{:^63}'.format('Sorteio'),
              '===' * 21, '  A ordem de apresentação é: \n', sep="\n")

        for i in range(len(a)):
            print('    {}º - {}'.format(i+1, a[i]))

        print('---' * 21,
              '{:>63}'.format('Autor: Francisco Camello'), sep="\n")


students = ['Joao', 'Maria', 'Jose', 'Joaquim', 'Madalena', 'Enyel']
Chicken_Dinner(students).print_result()
