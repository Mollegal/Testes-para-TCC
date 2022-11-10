import tkinter
import customtkinter


#Definindo Tema

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

#Cirando App

PMDV =  customtkinter.CTk()
PMDV.geometry("600x500")
PMDV.title("Programa Mol de Dimensionamento de Vigas")

#Separando Colunas e Linha para frames

PMDV.grid_columnconfigure(1, weight=1)
PMDV.grid_rowconfigure(0, weight=1)

#Frame da Esquerda

l_frame = customtkinter.CTkFrame(master=PMDV, width=200, corner_radius=0)
l_frame.grid(column=0, row=0, sticky="nswe")

#Frame da Direita

d_frame = customtkinter.CTkFrame(master=PMDV)
d_frame.grid(column=1, row=0, padx=5, pady=5, sticky="nswe")

#---Def's---#



#-----------#

PMDV.mainloop()