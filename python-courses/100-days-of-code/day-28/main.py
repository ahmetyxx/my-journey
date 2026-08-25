from pydoc import text
import tkinter as tk



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    
    if reps in [1,3,5,7]:  
        count_down(5 * 2)
    elif reps ==8:
        count_down(20)
        
    elif reps in [2,4,6]:
        count_down(5)
    reps+=1
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min= count//60
    count_sec= count % 60
    
    if len(str(count_sec)) < 2:
        count_sec=f"0{count_sec}"
    
    if count==0:
            start_timer()
    
    canvas.itemconfig(cnv_timer,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)
    


# ---------------------------- UI SETUP ------------------------------- #

window=tk.Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

tomato_img=tk.PhotoImage(file="tomato.png")



canvas=tk.Canvas(width=270,height=310,bg=YELLOW,highlightthickness=0)
canvas.create_image(150,170, image=tomato_img)
cnv_timer=canvas.create_text(150,180,text="00:00",fill="white",font=(FONT_NAME,28,"bold"))
canvas.create_text(155,16,text="Timer",font=(FONT_NAME,35,""),fill=GREEN)
canvas.grid(column=1,row=0)



btn_reset=tk.Button(text="reset")#,command=reset_timer)
btn_reset.grid(column=0,row=1)

btn_start=tk.Button(text="start", command=start_timer)
btn_start.grid(column=2,row=1)

lbl_check=tk.Label(text="✓",fg=GREEN,font=(FONT_NAME,15,""),bg=YELLOW)
lbl_check.grid(column=1,row=3)

window.mainloop()