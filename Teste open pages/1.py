import tkinter
from tkinter import filedialog
import customtkinter
import os
import sys

janela = customtkinter.CTk()
janela.geometry("400x400")
janela.title("Testes")

def open():
    Path = filedialog.askopenfilename()
    os.system('"%s"' %)
    

button = customtkinter.CTkButton(master=janela, text="Open 2", command=open).pack()



janela.mainloop()