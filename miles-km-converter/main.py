import tkinter as tk

def milesToKms():
    miles = float(miles_input.get())
    km = 1.609 * miles
    kilometer_result_label.config(text=f"{km}")

window = tk.Tk()
window.title("Miles to kilometer converter")
window.config(padx=20, pady=20)

#Creating widgets
miles_input = tk.Entry() 
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text = "Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text = "is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tk.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tk.Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = tk.Button(text="Calculate", command=milesToKms)
calculate_button.grid(column=1, row=2)








window.mainloop()