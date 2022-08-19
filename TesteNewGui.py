import tkinter
import customtkinter

#definindo padrões
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#criando classe e iniciando janela
class App(customtkinter.CTk):
    
    WIDTH = 500
    HEIGHT = 300
    
    def __init__(self):
        super().__init__()
        
        self.title("Teste New GUI.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        
        #Criar 2 frames
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #frame esquerda
        frame_left = customtkinter.CTkFrame(master=self, width=200, corner_radius=0)
        frame_left.grid(column=0, row=0, sticky="nswe")
        frame_left.columnconfigure((0, 1), weight=1)
        
        #frame direita
        frame_right = customtkinter.CTkFrame(master=self)
        frame_right.grid(column=1, row=0, padx=20, pady=20, sticky="nswe")
        
        #Prenchendo Frame da esquerda
        #-texto inicial
        self.label_1 = customtkinter.CTkLabel(master=frame_left, text="Parâmetros Viga",
                                             text_font=("Roboto Medium", -16))
        self.label_1.grid(column=0, columnspan=2, row=1, padx=10, pady=10)
        
        #-dados Mk
        self.label_mk = customtkinter.CTkLabel(master=frame_left, text="Mk",
                                              text_font=("Roboto Medium", -16))
        self.label_mk.grid(column=0, row=2, padx=10, pady=10)
        self.entry_mk = customtkinter.CTkEntry(master=frame_left, width=80)
        self.entry_mk.grid(column=1, row=2, padx=10, pady=10)
        
        #
        


    #criando janela
if __name__ == "__main__":
    app = App   ()
    app.mainloop()
