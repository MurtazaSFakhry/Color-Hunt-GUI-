import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os
import pyperclip

root = tk.Tk()
root.title("Color Picker")
root.geometry("800x470+100+100")
root.configure(bg="#F8F1F1")
root.resizable(False, False)

filename = ""

def show_image():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='Select Image File',
        filetype=(('PNG file', '*.png'), ('JPG file', '*.jpg'), ("ALL file", '*.txt'))
    )
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=310, height=270)
    lbl.image = img

def find_color():
    if not filename:
        return

    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=11)
    colors = []

    for rgb in palette:
        color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        colors.append(color)

    colors_section.itemconfig(ids[0], fill=colors[0])
    colors_section.itemconfig(ids[1], fill=colors[1])
    colors_section.itemconfig(ids[2], fill=colors[2])
    colors_section.itemconfig(ids[3], fill=colors[3])
    colors_section.itemconfig(ids[4], fill=colors[4])

    colors_section2.itemconfig(ids[5], fill=colors[5])
    colors_section2.itemconfig(ids[6], fill=colors[6])
    colors_section2.itemconfig(ids[7], fill=colors[7])
    colors_section2.itemconfig(ids[8], fill=colors[8])
    colors_section2.itemconfig(ids[9], fill=colors[9])

    for i in range(10):
        hex_labels[i].config(text=colors[i])

    print(*colors, sep='\n')


def copy_hex(hex_code):
    pyperclip.copy(hex_code)

colors = ["#b8255f", "#db4035", "#ff9933", "#fad000", "#afb83b",
          "#7ecc49", "#299438", "#6accbc", "#158fad", "#14aaf5"]

frame = tk.Frame(root, width=700, height=370, bg="#fff")
frame.place(x=50, y=50)

logo = ImageTk.PhotoImage(file="color1.png")
tk.Label(frame, text="Color Finder", font="arial 25 bold", bg="white").place(x=30, y=10)

# Colors section 1
colors_section = tk.Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors_section.place(x=20, y=90)

ids = []
hex_labels = []

for i in range(5):
    id_ = colors_section.create_rectangle((10, 10 + 50 * i, 50, 50 + 50 * i), fill=colors[i])
    hex_label = tk.Label(colors_section, text=colors[i], fg="#000", font="arial 12 bold", bg="white")
    hex_label.place(x=60, y=15 + 50 * i)
    copy_button = tk.Button(colors_section, text="Copy", command=lambda hex_code=colors[i]: copy_hex(hex_code))
    copy_button.place(x=110, y=15 + 50 * i + 15)
    ids.append(id_)
    hex_labels.append(hex_label)

# Colors section 2
colors_section2 = tk.Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors_section2.place(x=180, y=90)

for i in range(5, 10):
    id_ = colors_section2.create_rectangle((10, 10 + 50 * (i - 5), 50, 50 + 50 * (i - 5)), fill=colors[i])
    hex_label = tk.Label(colors_section2, text=colors[i], fg="#000", font="arial 12 bold", bg="white")
    hex_label.place(x=60, y=15 + 50 * (i - 5))
    copy_button = tk.Button(colors_section2, text="Copy", command=lambda hex_code=colors[i]: copy_hex(hex_code))
    copy_button.place(x=110, y=15 + 50 * (i - 5) + 15)
    ids.append(id_)
    hex_labels.append(hex_label)

# Select image
select_image = tk.Frame(frame, width=340, height=350, bg="#d6dee5")
select_image.place(x=350, y=10)

f = tk.Frame(select_image, bd=3, bg="black", width=320, height=280, relief=tk.GROOVE)
f.place(x=10, y=10)

lbl = tk.Label(f, bg="black")
lbl.place(x=0, y=0)

tk.Button(select_image, text="Select Image", width=12, height=1, font="arial 14 bold", command=show_image).place(x=10, y=300)
tk.Button(select_image, text="Find Colors", width=12, height=1, font="arial 14 bold", command=find_color).place(x=176, y=300)

root.mainloop()
