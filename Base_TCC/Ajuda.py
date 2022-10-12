import tkinter
import customtkinter

def ajudapp():
    
    #Definindo Tema
    
    #Criando janela
    ajuda = customtkinter.CTk()
    ajuda.geometry("400x400")
    ajuda.title("Ajuda")
    
    #adicionando imagem
    label = customtkinter.CTkLabel(master=ajuda, text="teste")
    label.pack()


    ajuda.mainloop()