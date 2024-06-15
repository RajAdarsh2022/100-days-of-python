from tkinter import *
import requests

def show_quote(quote):
    global quote_text
    canvas.delete(quote_text)
    quote_text = canvas.create_text(150, 207, text=f"{quote}", width=250, font=("Arial", 30, "bold"), fill="white")

def get_quote():
    kanye_quote = "Default quote"
    try:
        response = requests.get(url="https://api.kanye.rest")
        if response.status_code != 200:
            response.raise_for_status()
        json_data = response.json()
        kanye_quote = json_data.get("quote")
        print(kanye_quote)
        show_quote(kanye_quote)
        
    except Exception as error:
        print(f"An error occured: {error}")

    



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()