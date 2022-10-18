import tkinter
import customtkinter
from PIL import Image, ImageTk

def ajudapp():
    
    #Definindo Tema
    
    #Criando janela
    ajuda = customtkinter.CTk()
    ajuda.geometry("400x400")
    ajuda.title("Ajuda")
    
    #Paramentros Imagens
    imgteste = tkinter.PhotoImage(file="./Images/Teste.jpg")
    
    
    #adicionando imagem
    label = customtkinter.CTkLabel(master=ajuda, image="imgteste")
    label.pack()


    ajuda.mainloop()