import tkinter as tk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 100
SHORT_BREAK_MIN = 20
LONG_BREAK_MIN = 40
CANVAS_WIDTH = 250
CANVAS_HEIGHT = 250

time_left = WORK_MIN
timer_id = None

timer_signal = {
    "work" : False,
    "short-break" : False,
    "long-break" : False,
}

total_sessions = 0
number_of_sets = 0
number_of_sessions = 0
current_status = "work" 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def updateSessionData():
    """Updates the session data upon successful completion of work duration"""
    global total_sessions
    global number_of_sets
    global number_of_sessions

    number_of_sets = total_sessions // 4
    number_of_sessions = total_sessions % 4
    set_count_label.config(text=f"No. of sets done: {number_of_sets}")
    session_count_label.config(text=f"No. of sessions done: {number_of_sessions}")


def updateCurrentStatus(status):
    """Updates the status whether it is work-duration/short-break/long-break and changes the timer accordingly"""
    global current_status
    global time_left
    global timer_signal
    global timer_id

    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None

    current_status = status
    timer_signal[current_status] = True
    current_status_label.config(text=f"Current status is: {current_status}")

    if current_status == "work":
        time_left = WORK_MIN
    elif current_status == "short-break":
        time_left = SHORT_BREAK_MIN
    else:
        time_left = LONG_BREAK_MIN
    changeCounter()


def getCorrespondingTime(time_left):
    minutes_left = time_left // 60
    seconds_left = time_left % 60
    if minutes_left < 10:
        minutes_left = '0' + str(minutes_left)
    if seconds_left < 10:
        seconds_left = '0' + str(seconds_left)
    time_string  = f"{minutes_left}:{seconds_left}"
    return time_string

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def changeCounter():
    global time_left
    global timer_signal
    global total_sessions
    global current_status
    global timer_id

    if timer_signal[current_status] == True:
        if time_left > 0:
            canvas.itemconfig(timer_text, text=getCorrespondingTime(time_left))
            time_left -= 1
            timer_id = window.after(1000, changeCounter)
        else:
            if current_status == "work":
                timer_signal[current_status] = False
                total_sessions += 1
                updateSessionData()
                if total_sessions % 4 == 0:
                    updateCurrentStatus("long-break")
                else:
                    updateCurrentStatus("short-break")
            else:
                timer_signal[current_status] = False
                updateCurrentStatus("work")

def startTimer():
    global timer_signal
    timer_signal[current_status] = True
    changeCounter()

def stopTimer():
    global timer_signal
    global timer_id

    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None
    timer_signal[current_status] = False

def resetTimer():
    """Resets everything to the initial stage"""
    stopTimer()
    global time_left
    global current_status
    global timer_signal

    global total_sessions
    global number_of_sets
    global number_of_sessions
    
    for key in timer_signal:
        timer_signal[key] = False
    
    total_sessions = 0
    number_of_sets = 0
    number_of_sessions = 0
    
    current_status = "work"
    timer_signal[current_status] = True
    time_left = WORK_MIN
    canvas.itemconfig(timer_text, text=getCorrespondingTime(time_left))
    updateSessionData()
    current_status_label.config(text=f"Current status is: {current_status}")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro App")
window.geometry("600x600")

#Creating grid layout
window.rowconfigure(0, weight = 1, uniform= 'a')
window.rowconfigure(1, weight = 4, uniform= 'a')
window.rowconfigure((2,3), weight = 1, uniform= 'a')
window.columnconfigure(0, weight = 1, uniform='a')
window.columnconfigure(1, weight = 2, uniform='a')
window.columnconfigure(2, weight = 1, uniform='a')

#Creating widgets
top_section = tk.Label(window, background=YELLOW)
intro_label = tk.Label(top_section, text="Welcome to the Pomodoro App!")
set_count_label = tk.Label(top_section, text=f"No. of sets done: {number_of_sets}")
session_count_label = tk.Label(top_section, text=f"No. of sessions done: {number_of_sessions}")

label1 = tk.Label(window, text="Hi-there!", background=PINK)
label2 = tk.Label(window, text="Hi-there-2!", background=PINK)

start_button = tk.Button(window, text="Start", command=startTimer)

label4 = tk.Label(window, background=RED)
current_status_label = tk.Label(label4, text=f"Current status is: {current_status}")

reset_button = tk.Button(window, text="Reset", command=resetTimer)
stop_button = tk.Button(window, text="Stop Timer", command=stopTimer)

canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
tomato_img = tk.PhotoImage(file="images/tomato.png")
canvas.create_image(0, 0, anchor='nw', image=tomato_img)
timer_text = canvas.create_text(125, 125, text=getCorrespondingTime(time_left), fill='white', font=(FONT_NAME, 35, 'bold'))

#Placing items on the window
intro_label.pack(side='top', expand=True, fill='x')
set_count_label.pack(side='top', expand=True, fill='x')
session_count_label.pack(side='top', expand=True, fill='x')

top_section.grid(row=0, column=0, columnspan=3, sticky='ewns')
label1.grid(row=1, column=0, sticky='ewns')
label2.grid(row=1, column=2, sticky='ewns')
start_button.grid(row=2, column=0)

current_status_label.pack(side='top', expand=True, fill='x')
label4.grid(row=2, column=1, sticky='ewns')

reset_button.grid(row=2, column=2)
stop_button.grid(row=3, column=1, sticky='ew')
canvas.grid(row=1, column=1)

window.mainloop()

