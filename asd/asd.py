Import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image



root = ctk.CTk()

transparent_image = ImageTk.PhotoImage(Image.open("image-url/path"))

image_label = ctk.CTkLabel(root, image=transparent_image)
image_label.pack()

#Note : I'm not sure if CTkLabel has an image argument(CTkButton has one)
#if not : Then use this instead of CTkLabel
label = tk.Label(root, image = img)
label.pack()


root.mainloop()