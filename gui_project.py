
#The step one to run this program is type "pip install --user currencyconverter" in your terminal and add it to environment path vairables.

from currency_converter import CurrencyConverter

obj=CurrencyConverter()

import tkinter as tk

def clicked():
    amnt=int(entry1.get())
    cr1=entry2.get()
    cr2=entry3.get()
    result=str(int(obj.convert(amnt,cr1,cr2)))
    answer=tk.Label(screen,text="The desired amount is: "+result,font="Times 20",bg="LightYellow2",fg="maroon1").place(x=100,y=502)
    
screen=tk.Tk()
screen.geometry("1500x700")
screen["background"]="light blue"


title=tk.Label(screen,text="Currency Converter",font="Times 40 bold",bg="misty rose",fg="steel blue").place(x=550,y=0)

amount=tk.Label(screen,text="Enter the amount:",font="Times 20",bg="LightYellow2",fg="forest green").place(x=100,y=102)
entry1=tk.Entry(screen)

currency1=tk.Label(screen,text="Enter the currency of given amount:",font="Times 20",bg="LightYellow2",fg="forest green").place(x=100,y=202)
entry2=tk.Entry(screen)

currency2=tk.Label(screen,text="Enter the desired currency of amount:",font="Times 20",bg="LightYellow2",fg="forest green").place(x=100,y=302)
entry3=tk.Entry(screen)

enter=tk.Button(screen,text="Go !!",font="Times 20",command=clicked,bg="gray90").place(x=550,y=402)
entry1.place(x=350,y=110)
entry2.place(x=550,y=210)
entry3.place(x=550,y=310)

screen.mainloop()