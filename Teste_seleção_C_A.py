import tkinter
import customtkinter



App = customtkinter.CTk()
App.geometry("320x200")
App.title("TEste Menu concreto")

#Equação
def resultado_concreto():
    Mpa = float(Menu_Concreto.get())
    Fcd= (Mpa*0.85)/1.14
    Label_resultado.config(text=round(Fcd, 1))

#MenuBox
Menu_Concreto = customtkinter.CTkComboBox(App, values=["20", "25", "30"])
Menu_Concreto.grid(column=0, row=0, padx=10, pady=10)

#Botão
B_resultado = customtkinter.CTkButton(App, text="Resultado", command=resultado_concreto)
B_resultado.grid(column=0, row=1, padx=10, pady=10)

#Label
Label_resultado = customtkinter.CTkLabel(App, text="")
Label_resultado.grid(column=0, row=3, padx=1, pady=10)

App.mainloop()