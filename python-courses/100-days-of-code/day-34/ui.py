from tkinter import *

THEME_COLOR = "#375463"
FONT="Arial",15,"italic"

class Quizzİnterface:
    def __init__(self):
        self.window= Tk()
        self.window.config(padx=20,pady=20,bg=THEME_COLOR,)
        self.window.title("Quizzler")
        
        self.score=Label(text="Score: 0",bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1,pady=20)
        
        self.true_img=PhotoImage(file=r"images\true.png")
        self.false_img=PhotoImage(file=r"images\false.png")
        
        self.canvas=Canvas(width=300,height=250)
        self.canvas.grid(row=1,column=0,columnspan=2)
        self.question_text=self.canvas.create_text(150,125,text="blank",font=(FONT),fill=THEME_COLOR)
        
        self.true_button=Button(image=self.true_img,borderwidth=0.1)
        self.true_button.grid(row=2,column=0,pady=20)
        self.false_button=Button(image=self.false_img,borderwidth=0.1)
        self.false_button.grid(row=2,column=1,pady=20)
        
        self.window.mainloop()