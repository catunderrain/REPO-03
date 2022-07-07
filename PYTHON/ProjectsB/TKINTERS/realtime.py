from tkinter import *
from tkinter.ttk import *
from time import strftime
main = Tk()
main.title('Time')


def clock():
    tick = strftime('%H%M%S')
    clock_label .config(text=tick)
    clock_label .after(1000, clock)


clock_label = Label(main, font=('courier', 80),
                    background='black', foreground='white')
clock_label.pack(anchor='center')
clock()
mainloop()
