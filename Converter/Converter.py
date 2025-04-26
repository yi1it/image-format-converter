import tkinter as tk
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog
from PIL import Image
import os
import sys

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(__file__)
icon_path = os.path.join(application_path, "icon.ico")

root = TkinterDnD.Tk()
root.title("Resim Format Dönüştürücü")
root.geometry("600x400")

try:
    root.iconbitmap(icon_path)
except:
    pass

root.configure(bg="#252525")

root.minsize(350, 400)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

frame = ctk.CTkFrame(root, fg_color="#252525")
frame.place(relx=0.5, rely=0.5, anchor="center")

selected_file_label = ctk.CTkLabel(frame, text="Seçilen dosya: Yok", fg_color="#252525", text_color="white", wraplength=400)
selected_file_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

selected_format_label = ctk.CTkLabel(frame, text="Dönüştürülecek format: JPG", fg_color="#252525", text_color="white")
selected_format_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

selected_file = None

def open_file():
    global selected_file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.webp;*.svg")])
    if file_path:
        selected_file = file_path
        file_name = os.path.basename(file_path)
        selected_file_label.configure(text=f"Seçilen dosya: {file_name}")
        convert_button.configure(state=tk.NORMAL)

format_options = ["JPG", "PNG", "WEBP", "BMP", "ICO"]
selected_format = tk.StringVar(value="JPG")

format_menu = ctk.CTkOptionMenu(frame, values=format_options, variable=selected_format, command=lambda _: update_format_label())
format_menu.grid(row=2, column=0, pady=10, padx=10)

def update_format_label():
    selected_format_label.configure(text=f"Dönüştürülecek format: {selected_format.get()}")

open_button = ctk.CTkButton(frame, text="Dosya Seç", command=open_file)
open_button.grid(row=3, column=0, pady=20, padx=10)


def convert_image():
    global selected_file
    if selected_file:
        img = Image.open(selected_file)
        new_format = selected_format.get().lower()
        file_name, file_extension = os.path.splitext(selected_file)
        output_file = f"{file_name}_converted.{new_format}"

        if new_format == 'ico':
            img = img.convert("RGBA")
            img.save(output_file, format="ICO")
        else:
            img = img.convert("RGB")
            if new_format == 'jpg':
                new_format = 'jpeg'
            img.save(output_file, new_format.upper())

        selected_file_label.configure(text=f"Dosya kaydedildi: {output_file}")

convert_button = ctk.CTkButton(frame, text="Dönüştür", command=convert_image, state=tk.DISABLED)
convert_button.grid(row=4, column=0, pady=20, padx=10)

footer_label = ctk.CTkLabel(root, text="by yigitat", fg_color="#252525", text_color="white", font=("Arial", 10))
footer_label.pack(side="bottom", pady=5)

root.mainloop()
