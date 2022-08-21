from cgitb import text
import tkinter
import customtkinter


#padrão

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#Janela

janela = customtkinter.CTk()
janela.title("Teste-Concreto e Aço")


#concreto

Bconcreto = customtkinter.CTkOptionMenu(master=janela, values=["C20", "C25", "C30"])
Bconcreto.grid(column=0, row=0, padx=20, pady=20)

Testesaida = customtkinter.CTkLabel(master=janela, text="")
Testesaida.grid(column=0, row=1, padx=20, pady=20)






janela.mainloop()