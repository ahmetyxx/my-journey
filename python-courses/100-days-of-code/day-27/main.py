import tkinter

window=tkinter.Tk()
window.title("my GUI")
window.minsize(width=600,height=500)

label=tkinter.Label(text="i am not telling the truth", font=("arial",24,"bold"))
label.grid(column=0,row=0)

entry=tkinter.Entry(width=20)
entry.grid(column=3,row=2)

def button_action():
    label.config(text=entry.get())
    
print(entry.get())
    
button=tkinter.Button(text="click me",command=button_action)
button.grid(column=1,row=1)
button1=tkinter.Button(text="dont click me",command=button_action)
button1.grid(column=2,row=0)
    
window.mainloop()