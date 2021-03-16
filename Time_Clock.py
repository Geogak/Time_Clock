from tkinter import *


root = Tk()
root.title("Time Clock")

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

def launch_pin_window():
    global text_entry 
    global debug
    pin_window = Tk()
    pin_window.title("Time Clock")
    #create the text entry field
    text_entry =  Entry(pin_window, show = "*", width = 35, borderwidth = 1)
    #text_entry.grid(row = 0, column = 0, columnspan = 3 )
    #debug field
    debug = Entry(pin_window,  width = 35, borderwidth = 1)
    debug.grid(row = 6, column = 0, columnspan = 3 )
    #Define buttons
    button_1 = Button(pin_window, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
    button_2 = Button(pin_window, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
    button_3 = Button(pin_window, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
    button_4 = Button(pin_window, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
    button_5 = Button(pin_window, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
    button_6 = Button(pin_window, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
    button_7 = Button(pin_window, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
    button_8 = Button(pin_window, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
    button_9 = Button(pin_window, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
    button_0 = Button(pin_window, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
    button_ok = Button(pin_window, text = "OK", padx = 35, pady = 20, command = button_click_ok)
    button_x = Button(pin_window, text = "X", padx = 40, pady = 20, command = button_click_x)
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
    
button_NW = Button(root, text = "Pin Entry", command = launch_pin_window)
button_NW.grid(row = 1, column = 0, columnspan = 3)

root.mainloop() 