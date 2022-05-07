'''
Modulo que generara la matriz
'''
import random
import os
from .validations import Validations
# borrarPantalla = lambda: os.system ("cls")


def generator():
    Grid = [["" for x in range(9)] for y in range(9)]

    for i in range(25):  # numeros aleatorios que tendra la matriz
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        Grid[row][col] = str(num)

    return Grid


def tests(Matriz):
    '''
    validaciones para que la matriz sea resoluble
    o bien que no tenga numeros repetidos
    '''
    val = Validations(Matriz)
    test1 = val.check_columns()
    test2 = val.check_row()
    test3 = val.subframesCheck()
    test3 = (False not in test3[0]) and (
        False not in test3[1]) and (False not in test3[2])
    test4 = val.check_data()
    return (test1 and test2 and test3 and test4)


def matriz():
    '''
    Solo tendras que llamar a esta funcion para obtener la matriz
    no necesita recibir ningun parametro
    Aun falta optimizarlo pero pero siempre sera esta la funcion generadora
    '''
    Matriz = generator()
    is_valid = tests(Matriz)
    while not is_valid:
        Matriz = generator()
        is_valid = tests(Matriz)
    return Matriz
