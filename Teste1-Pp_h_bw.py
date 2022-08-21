from tkinter import *
from tkinter import ttk

#Opções da janela
openwindow = Tk()
openwindow.title("Calculo Pp")

padding = {'padx': 5, 'pady': 5}

#texto inicial
textoA = Label(openwindow, text="Preencha com os dados correspondentes de sua viga")
textoA.grid(column=0, row=0, padx=10, pady=10)

#operações
def Ppcalc():
    h = float(h_entry.get())
    bw = float(bw_entry.get())
    Pp = 1.0*h*bw*25.0 
    
    Pesoproprio.config(text=round(Pp))

#entrada de valores

h_entryText = Label(openwindow, text="Valor de 'h'")
h_entryText.grid(column=0, row=1, **padding)
h_entry = ttk.Entry(openwindow, textvariable="h")
h_entry.grid(column=1, row=1, **padding)

bw_entryText = Label(openwindow, text="Valor de 'bw'")
bw_entryText.grid(column=0, row=2, **padding)
bw_entry = ttk.Entry(openwindow, textvariable="bw")
bw_entry.grid(column=1, row=2, **padding)

#botão para resultado
botao = Button(openwindow, text="Calcular", command=Ppcalc)
botao.grid(column=0, row=3, **padding)

#resultados
Pesoproprio = Label(openwindow, text="")
Pesoproprio.grid(column=0, row=4, **padding)

openwindow.mainloop()