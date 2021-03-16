from tkinter import *


root = Tk()
root.title("Time Clock")

#create the text entry field
text_entry =  Entry(root, show = "*", width = 35, borderwidth = 1)
#text_entry.grid(row = 0, column = 0, columnspan = 3 )

#debug field
debug = Entry(root,  width = 35, borderwidth = 1)
debug.grid(row = 6, column = 0, columnspan = 3 )

def button_click(num):
    current = text_entry.get()
    text_entry.delete(0, END)
    text_entry.insert(0,str(current) + str(num))
    return

def button_click_ok():
    debug.delete(0, END)
    debug.insert(0, text_entry.get())
    text_entry.delete(0, END)
    return

def button_click_x():
    text_entry.delete(0, END)
    return

def new_window():
    root.destroy()
    window_2 =Tk()
    window_2.title("Time Clock")
    button_close = Button(window_2, text = "Close", command = window_2.destroy)
    button_close.pack()


#Define buttons
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_ok = Button(root, text = "OK", padx = 35, pady = 20, command = button_click_ok)
button_x = Button(root, text = "X", padx = 40, pady = 20, command = button_click_x)

button_NW = Button(root, text = "New Window", command = new_window)


#Draw buttons
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_x.grid(row = 4, column = 0)
button_0.grid(row = 4, column = 1)
button_ok.grid(row = 4, column = 2)

button_NW.grid(row = 5, column = 0, columnspan = 3)



root.mainloop() 