from tkinter import *
from tkinter import ttk
from logic.generatorBoard import matriz, tests


# crear tabla de sudoku y dibujar con tkinter
def main(Matriz):
    root = Tk()
    root.geometry("500x500")
    root.maxsize(500, 500)
    root.minsize(500, 500)
    root.title("Sudoku")
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

    # crear una un boton para verificar la solucion con la funcion tests
    button = ttk.Button(root, text="Verificar",
                        command=lambda: print(tests(Matriz)))
    button.grid(row=9, column=0, columnspan=9)
    button.config(width=20)

    message = ttk.Label(
        root, text="Presione el boton para verificar la solucion")
    message.grid(row=10, column=0, columnspan=9)

    root.mainloop()


main(matriz())
