from tkinter import *

def calculo():
    a = 2
    b = (a+a)
    
    seuvalor["text"] = b

janela = Tk()
janela.title("CPDP")
janela.geometry("400x200")

PMensagem = Label(janela, text="Bem Vindo ao CPDP (Calculadora de Pré Dimensionamento de Pilares)")
PMensagem.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Clique para receber o valor", command=calculo)
botao.grid(column=0, row=1, padx=10, pady=10)

chk1 = Checkbutton(janela, text="Já possui ND definido?")
chk1.grid(column=0, row=3, padx=10, pady=10)


seuvalor = Label(janela, text="")
seuvalor.grid(column=0, row=4, padx=10, pady=10)



janela.mainloop()