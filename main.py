from tkinter import *
from tkinter import ttk
from logic.generatorBoard import matriz, tests


# crear tabla de sudoku y dibujar con tkinter
def create_table(Matriz):
    root = Tk()
    root.geometry("500x500")
    root.title("Sudoku")
    root.resizable(0, 0)
    for i in range(9):
        for j in range(9):
            # crear una caja para cada numero
            entry = ttk.Entry(root, width=2, justify=CENTER)
            entry.grid(row=i, column=j)
            entry.config(font=("Arial", 20))
            entry.insert(0, Matriz[i][j])

            # Editar solo los numeros que no esten vacios
            if Matriz[i][j] != "":
                entry.config(state="disabled")
            else:
                entry.config(state="normal")

            # Meter los numeros en la matriz
            entry.bind("<KeyRelease>", lambda event, i=i, j=j:
                       change_value(event, i, j))

    root.mainloop()


create_table(matriz())
