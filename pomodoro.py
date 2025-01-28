#Building Pomodoro Timer

import tkinter as tk


WORK_TIME = 60* 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 20 * 60


window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50)


timer = None
is_running = False
time_left = WORK_TIME
current_session = "Work"
checks = 0

timer_label = tk.Label(text="60:00", font=("Arial", 40, "bold"))
timer_label.grid(row=0, column=0, columnspan=2, pady=20)


session_label = tk.Label(text="Work", font=("Arial", 20))
session_label.grid(row=1, column=0, columnspan=2)


checkmarks_label = tk.Label(font=("Arial", 20))
checkmarks_label.grid(row=3, column=0, columnspan=2)


def start_timer():
    global is_running
    if not is_running:
        is_running = True
        start_button.config(state="disabled")
        countdown()

start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0, pady=20)


def reset_timer():
    global time_left, current_session, checks, is_running, timer
    if timer:
        window.after_cancel(timer)
    is_running = False
    start_button.config(state="normal")
    time_left = WORK_TIME
    current_session = "Work"
    checks = 0
    timer_label.config(text="25:00")
    session_label.config(text="Work")
    checkmarks_label.config(text="")

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=1)


def countdown():
    global time_left, checks, current_session, timer, is_running

    if time_left > 0:
        time_left -= 1
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        timer = window.after(1000, countdown)
    else:
        if current_session == "Work":
            checks += 1
            checkmarks_label.config(text='✔' * checks)
            if checks % 4 == 0:
                time_left = LONG_BREAK
                current_session = "Break"
                checks = 0
            else:
                time_left = SHORT_BREAK
                current_session = "Break"
        else:
            time_left = WORK_TIME
            current_session = "Work"
        session_label.config(text=current_session)
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        countdown()

window.mainloop()
       
       

