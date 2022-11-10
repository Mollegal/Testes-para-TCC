import tkinter
import customtkinter
from PIL import ImageTk, Image

app = customtkinter.CTk()

pht = Image.open("teste.jpg")
img = ImageTk.PhotoImage(pht)
label = customtkinter.CTkLabel(master=app, Image=img)
label.pack()




app.mainloop()