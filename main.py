from helpers.nameHandler import *
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

class testGUI:
    def __init__(self,root):
        self.root = root
        print("Created instance of test")
    mainframe = ttk.Frame(root, padding="100")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    ttk.Label(mainframe, text="Helloyall").grid(column=0, row=0)


class MasterGUI:
    def __init__(self, root):
        print("Created instance of Master")
    #     # Set title of window
    #     root.title("EasyFin")
        
    #     # Mainframe is the opening frame, thats inside the root. Heres our setup
    #     mainframe = ttk.Frame(root, padding="100")
    #     mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    #     CURRENTMONTH = getCurrentMonth()
    #     self.curMonth = StringVar()
    #     self.curMonth.set(CURRENTMONTH)

    #     # If I wanted a label, say for the total costs for the month?
    #     self.welcomeString = StringVar()
    #     self.welcomeString.set("View " + CURRENTMONTH + " finances?")
    #     ttk.Label(mainframe, textvariable=self.welcomeString).grid(column=0, row=0)

    #     # Heres how we can create a Text Entry box that will set the month variable.
    #     # We set its parent to mainframe, and set where it will appear
    #     self.month = StringVar()
    #     month_entry = ttk.Combobox(mainframe, textvariable=self.month)
    #     #Triggers on any change to 
    #     month_entry.bind('<<ComboboxSelected>>', self.setMonth)
    #     # Need an array of months
    #     monthList = ('January', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    #     month_entry['values'] = monthList
    #     month_entry.state(["readonly"])

    #     self.selectMonth = StringVar()
    #     self.selectMonth.set("Select " + CURRENTMONTH)
    #     ttk.Button(mainframe, textvariable=self.selectMonth, command=self.tester).grid(column=0, row=4, sticky=(N,E,S,W))

    #     for child in mainframe.winfo_children():
    #         child.grid_configure(padx=5,pady=5)
    #     root.bind("<Return>", self.tester)  
    
    # def tester(self, *args):
    #     try:
    #         print("Clicked Button")
    #     except ValueError:
    #         pass
    # def setMonth(self, *args):
    #     try:
    #         CURRENTMONTH = self.month.get()
    #         self.curMonth.set(CURRENTMONTH)
    #         self.welcomeString.set("View " + CURRENTMONTH + " finances?")
    #         self.selectMonth.set("Select " + CURRENTMONTH)
    #     except ValueError:
    #         pass

root = Tk()
MasterGUI(root)
root.mainloop()