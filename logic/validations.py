'''
En este script estara la logica de nuestro juego, donde se veran
las validaciones:
1. Que el numero que coloquemos en una casilla no se repita
  1.1 Que no se repita en toda la fila
  1.2 Que no se repita en toda la columna
2.Verificar que los subcuadros no se repitan sus numeros ni que sean mayores a 9
Si todo esta bien, dejaremos pasar a las funciones de los componentes :)

board = [
  ["1","2","3","4","5","6","7","8","9"],
  ["2","","","","","","","",""],
  ["3","","","","","","","",""],
  ["4","","","","","","","",""],
  ["5","","","","","","","",""],
  ["6","","","","","","","",""],
  ["7","","","","","","","",""],
  ["8","","","","","","","",""],
  ["9","","","","","","","",""],
]

'''

board = [
    ["5", "3", "3", "", "7", "", "", "", ""],
    ["6", "7", "", "1", "9", "5", "", "", ""],
    ["", "9", "8", "", "", "", "", "6", ""],
    ["8", "", "", "", "6", "", "", "", "3"],
    ["4", "", "", "8", "", "3", "", "", "1"],
    ["7", "", "", "", "2", "", "", "", "6"],
    ["", "6", "", "", "", "", "2", "8", ""],
    ["", "", "", "4", "1", "9", "", "5", "5"],
    ["", "", "", "", "8", "", "", "7", "9"]
]

# matriz de 3x3


class Validations:
    def __init__(self, board):
        self._board = board
        self._invertedBoard = []

    def check_data(self):
        '''
        chequeo de la cantidad filas y columnas
        '''
        return len([row for row in self._board if len(row) == 9]) == 9

    def check_row(self, board=None):
        '''
        chequeamos las filas y si en una fila un elemento aparece más de una vez
        lo sustituimos por el string "invalid" y metemos todos estos datos en un array
        si entre estos datos surgio el string "invalid" retornamos false, indicando que
        el chequeo fallo
        '''
        BOARD = board if board != None else self._board
        return not "invalid" in ['invalid' if row.count(item) > 1 else item for row in BOARD for item in row if item != '']

    def check_columns(self):
        '''
        Para realizar esta funcion invertiremos la tabla de la siguiente forma:
        primero tomaremos el index de las columnas de la matriz,
        crearemos una array para aguardar los elementos de esta columna,
        luego obtendremos el indexs de las filas de la matriz,
        al array que creamos le agregaremos los column_index de cada fila
        y agregamos este array a una matriz que llamaremos invertedBoard
        '''
        for column_index in range(len(self._board[0])):
            column = []
            for row_index in range(len(self._board)):
                column.append(self._board[row_index][column_index])
            self._invertedBoard.append(column)
        return self.check_row(self._invertedBoard)

    def subframesCheck(self):
        '''
        tenemos 9 subcuadros = chequear de 3 en 3
        de las primeras 3 filas -> subcuadros del 0 al 3, 3 al 6, 6 al 9
        Ejemplo:
          board2 = [
          ["1","2","3"],
          ["5","4","6"],
          ["8","7","9"]
          ]
        '''
        result1 = self.subframe_check(0, 3)
        result2 = self.subframe_check(3, 6)
        result3 = self.subframe_check(6, 9)
        return [result1, result2, result3]

    def check_list(self, lista):
        '''
        funcion para chequear si una lista contiene los numeros del 1 al 9 y que no esten repetidos
        '''
        lista = [item for item in lista if item]
        for elemento in lista:
            if int(elemento) > 9:
                return False
            if lista.count(elemento) > 1:
                return False
        return True

    def subframe_check(self, start_index, end_index):
        '''
        # range(start_index,end_index) determinara el inicio y el fin de esta columna
        # el resultado de cada subcuadro se agregara a un array
        # retornamos el array con los resultados de cada subcuadro
        '''
        subcuadro = []
        resultado = []
        for row_index in range(0, 9):
            if row_index == 3 or row_index == 6:
                subcuadro.clear()
            for column_index in range(start_index, end_index):
                subcuadro.append(self._board[column_index][row_index])
                if len(subcuadro) == 9:
                    resultado.append(self.check_list(subcuadro))
        return resultado


# if __name__ == "__main__":
#     validations = Validations(board)
#     print(validations.check_data())
#     print(validations.check_row())
#     print(validations.check_columns())
#     print(validations.subframesCheck())
