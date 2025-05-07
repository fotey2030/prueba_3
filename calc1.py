import tkinter as tk

def click(valor):
    entrada.insert(tk.END, valor)

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Franco")

# Entrada
entrada = tk.Entry(ventana, width=20, font=("Arial", 18), bd=4, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones
botones = ['7', '8', '9', '/', '4', '5', '6', '*',
           '1', '2', '3', '-', '0', '.', '=', '+']

fila = 1
col = 0

for btn in botones:
    if btn == '=':
        comando = calcular
    else:
        comando = lambda x=btn: click(x)
    tk.Button(ventana, text=btn, width=5, height=2, font=("Arial", 14), command=comando).grid(row=fila, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        fila += 1

tk.Button(ventana, text="C", width=22, height=2, font=("Arial", 14), command=borrar).grid(row=fila, column=0, columnspan=4, padx=5, pady=5)

ventana.mainloop()
