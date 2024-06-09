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
CANVAS_WIDTH = 250
CANVAS_HEIGHT = 250

time_left = 300
timer_on = False
# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    stopTimer()
    global time_left
    time_left = 300
    canvas.itemconfig(timer_text, text=getCorrespondingTime(time_left))
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def getCorrespondingTime(time_left):
    minutes_left = time_left // 60
    seconds_left = time_left % 60
    if minutes_left < 10:
        minutes_left = '0' + str(minutes_left)
    if seconds_left < 10:
        seconds_left = '0' + str(seconds_left)
    time_string  = f"{minutes_left} : {seconds_left}"
    return time_string
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def changeCount():
    global time_left
    if time_left > 0 and timer_on == True:
        canvas.itemconfig(timer_text, text=getCorrespondingTime(time_left))
        time_left -= 1
        window.after(1000, changeCount)
    
def startTimer():
    global timer_on
    timer_on = True
    changeCount()

def stopTimer():
    global timer_on
    timer_on = False
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro App")
window.geometry("600x600")

#Creating grid layout
window.rowconfigure(0, weight = 1, uniform= 'a')
window.rowconfigure(1, weight = 4, uniform= 'a')
window.rowconfigure(((2,3,4)), weight = 1, uniform= 'a')
window.columnconfigure(0, weight = 1, uniform='a')
window.columnconfigure(1, weight = 2, uniform='a')
window.columnconfigure(2, weight = 1, uniform='a')

#Creating widgets
top_section = tk.Label(window, text="Welcome to the Pomodoro-app!", background='yellow')
label1 = tk.Label(window, text="Hi-there!", background='blue')
label2 = tk.Label(window, text="Hi-there-2!", background='blue')
start_button = tk.Button(window, text="Start", command=startTimer)
label4 = tk.Label(window, text="Hi-there-4!", background='red')
reset_button = tk.Button(window, text="Reset", command=resetTimer)
stop_button = tk.Button(window, text="Stop Timer" , command=stopTimer)
canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
tomato_img = tk.PhotoImage(file="images/tomato.png")
canvas.create_image(0,0, anchor='nw', image=tomato_img)
timer_text = canvas.create_text(125,125, text=f"{time_left}", fill='white', font=(FONT_NAME, 35, 'bold'))



#Placing items on the window
top_section.grid(row=0, column=0, columnspan=3, sticky='ewns')
label1.grid(row=1, column=0, sticky='ewns')
label2.grid(row=1, column=2, sticky='ewns')
start_button.grid(row=2, column=0)
label4.grid(row=2, column=1, sticky='ewns')
reset_button.grid(row=2, column=2)
stop_button.grid(row=3, column=1, sticky='ew')
canvas.grid(row=1, column=1)


# changeCount(time_left)


window.mainloop()