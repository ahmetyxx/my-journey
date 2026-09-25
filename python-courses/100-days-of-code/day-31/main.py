import tkinter as tk
import random as r
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"

window=tk.Tk()
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)
window.title("flashy")

previous_after=""
def generate_word():
    window.after_cancel(a)
    doc=pd.read_csv(r"data\french_words.csv")
    row_no=r.randint(0,len(doc.iloc[:,0]))
    canvas.itemconfig(word,text=doc.iloc[row_no,0])
    canvas.itemconfig(title,text="French")
    previous_after=window.after(3000)
    canvas.itemconfig(word,text=doc.iloc[row_no,1])
    canvas.itemconfig(title,text="English")

#images
ok_img=tk.PhotoImage(file=r"images\right.png")
wrong_img=tk.PhotoImage(file=r"images\wrong.png")
card_front_img=tk.PhotoImage(file=r"images\card_front.png")



canvas=tk.Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
canvas.create_image(400,263,image=card_front_img)
title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word=canvas.create_text(400,283,text="",font=("Ariel",60,"bold"))
 
 
 
#buttons
right_button=tk.Button(image=ok_img,command=generate_word)
right_button.grid(column=1,row=1)
wrong_button=tk.Button(image=wrong_img,command=generate_word)
wrong_button.grid(column=0,row=1)

generate_word()
window.mainloop()