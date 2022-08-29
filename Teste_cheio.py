import tkinter
import customtkinter


#criando janela
App = customtkinter.CTk()
App.geometry("880x480")
App.title("Testes Cheio")

#Criando frames
App.grid_columnconfigure(1, weight=1)
App.grid_rowconfigure(0, weight=1)

#Esquerda
left_frame = customtkinter.CTkFrame(master=App, width=200, corner_radius=0)
left_frame.grid(column=0, row=0, sticky="nswe")
left_frame.columnconfigure((0, 1), weight=1)

#frame direita
right_frame = customtkinter.CTkFrame(master=App)
right_frame.grid(column=1, row=0, padx=10, pady=10, sticky="nswe")

#-#-#-#-#-#-#-#-#-#-#-#-#

#Seleção de aço e concreto
label_concreto = customtkinter.CTkLabel(master=left_frame, text="Concreto")
label_concreto.grid(column=0, row=0, padx=20, pady=12)
menu_concreto = customtkinter.CTkComboBox(master=left_frame, values=["20", "25", "30"])
menu_concreto.grid(column=0, row=1, padx=10, pady=0)

label_aco = customtkinter.CTkLabel(master=left_frame, text="Aço")
label_aco.grid(column=1, row=0, padx=20, pady=12)
menu_aco = customtkinter.CTkComboBox(master=left_frame, values=["CA25", "CA50", "CA60"])
menu_aco.grid(column=1, row=1, padx=10, pady=10)

#entry valores
#mk
label_mk = customtkinter.CTkLabel(master= left_frame, text="Mk")
label_mk.grid(column= 0, row= 2, padx=10, pady=10)
entry_mk = customtkinter.CTkEntry(master= left_frame, justify="center")
entry_mk.grid(column=0, row=3, padx=10, pady=10)
#


App.mainloop()