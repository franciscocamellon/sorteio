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

print('===' * 21)
print('{:^63}'.format('Sorteio'))
print('===' * 21)


def chicken_dinner():
    """
    This function randomly shuffle the student's list.
    """
    students = ['Joao', 'Maria', 'Jose', 'Joaquim', 'Madalena', 'Enyel']
    order = []
    while len(students) > 0:
        random.shuffle(students)
        order.append(students.pop(0))
    return order


def print_result():
    """
    This function prints the order
    """
    a = chicken_dinner()
    print('  A ordem de apresentação é: \n')
    for i in range(len(a)):

        print('    {}º - {}'.format(i+1, a[i]))
    print('---' * 21, '{:>63}'.format('Autor: Francisco Camello'), sep="\n")


print_result()
