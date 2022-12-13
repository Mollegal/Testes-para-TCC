import tkinter
import customtkinter
import os
from PIL import ImageTk, Image

def ajuda():
    #Criando janela
    ajuda = customtkinter.CTk()
    ajuda.geometry("400x400")
    ajuda.title("Ajuda")

    pastaApp = os.path.dirname(__file__)

    img = ImageTk.PhotoImage(Image.open(pastaApp+"\\teste.jpg"))

    imglabel = customtkinter.CTkLabel(master=ajuda, image=img)
    imglabel.pack()

    ajuda.mainloop()