from tkinter import *
import requests

def GetQuote():
  Conn = requests.get("https://api.kanye.rest")
  Date = Conn.json()
  Quote = Date["quote"]
  Canvas_.itemconfig(QuoteText, text = Quote)

Window = Tk()
Window.title("Click on KanYe's Head...")
Window.config(padx = 50, pady = 50)

Canvas_ = Canvas(width = 300, height = 414)
BGImg = PhotoImage(file = "BGQuote.png")
Canvas_.create_image(150, 207, image= BGImg)
QuoteText = Canvas_.create_text(150, 207, text = "Kanye Quote Goes HERE", width = 250, font = ("Arial", 15, "bold"), fill = "white")
Canvas_.grid(row = 0, column = 0)

KanYeImg = PhotoImage(file =  "KanYeHead.png")
KanYeButton = Button(image = KanYeImg, highlightthickness = 0, command = GetQuote, borderwidth = 0)
KanYeButton.grid(row = 1, column = 0)

Window.mainloop()