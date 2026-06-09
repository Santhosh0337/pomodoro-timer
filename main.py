from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    if timer:
        window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(canvas_text, text="00:00")
    tick_label.config(text="")
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds=WORK_MIN*60
    short_break_seconds=SHORT_BREAK_MIN*60
    long_break_seconds=LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break_seconds)
        timer_label.config(text="Long Break",fg=PINK)

    elif reps%2==0:
        count_down(short_break_seconds)
        timer_label.config(text="Break",fg=RED)
    else :
        count_down(work_seconds)
        timer_label.config(text="Work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_minutes= math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds <10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(canvas_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for i in range(work_sessions):
            mark+="✓"
        tick_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #



#Window Creation:
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)


#Canvas Creation:
canvas= Canvas(window, width=200, height=224,bg=YELLOW,highlightthickness=0)
photo =PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo)
canvas_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,33,"bold"))
canvas.grid(row=1, column=1)

#Label 1 Timer Text:
timer_label=Label(text="Timer",font=(FONT_NAME,40,"bold"),bg=YELLOW,fg=GREEN)
timer_label.grid(row=0, column=1)

#Label 2 Tick Symbol ✓:
tick_label=Label(font=(FONT_NAME,20,"bold"),bg=YELLOW,fg=GREEN)
tick_label.grid(row=3, column=1)

#Button 1 Start:
start_button=Button(text="Start",command=start_timer)
start_button.grid(row=2, column=0)

#Button 2 Reset:
reset_button=Button(text="Reset",command=reset)
reset_button.grid(row=2, column=2)






window.mainloop()