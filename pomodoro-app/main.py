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
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro App")
window.geometry("800x600")

#Creating grid layout
window.rowconfigure(0, weight = 1, uniform= 'a')
window.rowconfigure(1, weight = 2, uniform= 'a')
window.rowconfigure(2, weight = 1, uniform= 'a')
window.columnconfigure(0, weight = 1, uniform='a')
window.columnconfigure(1, weight = 2, uniform='a')
window.columnconfigure(2, weight = 1, uniform='a')

#Creating widgets
top_section = tk.Label(window, text="Welcome to the Pomodoro-app!", background='yellow')
label1 = tk.Label(window, text="Hi-there!", background='blue')
label2 = tk.Label(window, text="Hi-there-2!", background='blue')
label3 = tk.Label(window, text="Hi-there-3!", background='green')
label4 = tk.Label(window, text="Hi-there-4!", background='red')
label5 = tk.Label(window, text="Hi-there-5!", background='green')
canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
tomato_img = tk.PhotoImage(file="images/tomato.png")
canvas.create_image(0,0, anchor='nw', image=tomato_img)



#Placing items on the window
top_section.grid(row=0, column=0, columnspan=3, sticky='ewns')
label1.grid(row=1, column=0, sticky='ewns')
label2.grid(row=1, column=2, sticky='ewns')
label3.grid(row=2, column=0, sticky='ewns')
label4.grid(row=2, column=1, sticky='ewns')
label5.grid(row=2, column=2, sticky='ewns')
canvas.grid(row=1, column=1)




window.mainloop()