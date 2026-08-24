import tkinter as tk

window=tk.Tk()
window.title("mile to kilometer")
window.minsize(width=300,height=300)
window.config(padx=100,pady=50)

mile_field=tk.Entry()
mile_field.focus()
mile_field.grid(column=1,row=0,padx=5)


mile_label=tk.Label(text="Miles")
mile_label.grid(column=2,row=0)

km_is_equal=tk.Label(text="is equal to")
km_is_equal.grid(column=0,row=1)
km_count=tk.Label(text="0")
km_count.grid(column=1,row=1)
km_km=tk.Label(text="km")
km_km.grid(column=2,row=1)

def calculate():
    mile=float(mile_field.get())
    result=mile*1.609344
    km_count.config(text=str(round(result,2))) 

button=tk.Button(text="caculate",command=calculate)
button.grid(column=1,row=2)

window.mainloop()