from tkinter import * 

window = Tk()

def convert_kilos():
    pounds = float(kilos_value.get()) * 1.6
    t1.insert(END , pounds)
    ounces = float(kilos_value.get()) ** 1.6
    t2.insert(END , ounces)
    grams = float(kilos_value.get()) ** 100
    t3.insert(END , grams)



b1 = Button(window , text = "Convert",command = convert_kilos)

b1.grid(row = 0 ,column = 10)

kilos_value = StringVar()

kilos = Entry(window , textvariable = kilos_value)

kilos.grid(row = 0 , column = 0)

t1 = Text(window , height = 1 , width = 10)

t1.grid(row = 0 , column = 3)

t2 = Text(window , height = 1 , width = 10)

t2.grid(row = 0, column = 6)

t3 = Text(window , height = 1 , width = 10)

t3.grid(row = 0, column = 8)

window.mainloop()

