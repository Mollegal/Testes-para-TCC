import tkinter
from tkinter import DoubleVar, ttk
import customtkinter

#definindo padrões
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#criando janela
app = customtkinter.CTk()
app.geometry("260x300")
app.title("Entry Testes.py")

#variavel
def calculo():
    Mk = DoubleVar(entry_1.get())
    Md = Mk*1.14*100.00

    label_2.config(text=Md)

#frame
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(column=0, row=0, pady=20, padx=20)
frame_2 = customtkinter.CTkFrame(master=app)
frame_2.grid(column=0, row=1, padx=20, pady=20)

#entry com label
label_1 = customtkinter.CTkLabel(master=frame_1, text="Mk")
label_1.grid(column=0, row=0, padx=10, pady=10)
entry_1 = customtkinter.CTkEntry(master=frame_1, width=40, textvariable="")
entry_1.grid(column=1, row=0, padx=10, pady=10)

#botão
button_1 = customtkinter.CTkButton(master=frame_1, text="Resultado", command=calculo)
button_1.grid(column=0, columnspan=2, row=1, padx=10, pady=10)

#resultado
label_2 = customtkinter.CTkLabel(master=frame_2, text="")
label_2.pack(padx=10, pady=10)





app.mainloop()