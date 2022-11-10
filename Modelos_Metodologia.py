import tkinter
import customtkinter

#-----Def's-----#

def button_event():
    fck = float(cbox_concreto.get())
    fcd = fck/1.4
    fyk = float(cbox_aco.get())
    fyd = fyk/1.4
    print("o Fcd é ", fcd, " e o Fyd é ", fyd)
    


#-----Def's-----#-

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
l_frame.grid_rowconfigure(9, minsize=700)

#Frame da Direita

d_frame = customtkinter.CTkFrame(master=PMDV)
d_frame.grid(column=1, row=0, padx=5, pady=5, sticky="nswe")


#--Conteudo Frame Esquerda--#

#ComboBox Aço e Concreto
label_concreto = customtkinter.CTkLabel(master=l_frame, text="Concreto")
label_concreto.grid(column=0, row=0, padx=20, pady=12)
cbox_concreto = customtkinter.CTkComboBox(master=l_frame, values=["20", "25", "30"])
cbox_concreto.grid(column=0, row=1, padx=10, pady=10)

label_aco = customtkinter.CTkLabel(master=l_frame, text="Aço")
label_aco.grid(column=1, row=0, padx=20, pady=12)
cbox_aco = customtkinter.CTkComboBox(master=l_frame, values=["25", "50", "60"])
cbox_aco.grid(column=1, row=1, padx=10, pady=10)

#botão resultado
resultado_b = customtkinter.CTkButton(master=l_frame, text="Resultado", command=button_event)
resultado_b.grid(column=0, columnspan= 2, row=9, padx=10, pady=10)



PMDV.mainloop()