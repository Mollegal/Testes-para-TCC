import tkinter
import customtkinter

def ajudapp():
    
    #Definindo Tema
    
    #Criando janela
    ajuda = customtkinter.CTk()
    ajuda.geometry("400x400")
    ajuda.title("Ajuda")

    label = customtkinter.CTkLabel(master=ajuda, text="Olá")
    label.pack()

    ajuda.mainloop()