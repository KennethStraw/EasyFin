from helpers.nameHandler import *
from helpers.createdb import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import sqlite3
import time

class MasterGUI:
    def __init__(self, app):
        # Set title of window
        app.title("Input Username to Connect DB")
        #app.title("EasyFin")
        self.Username = ""
                
        # Create a simple Username input to connect to DB 
        self.dbEntryFrame = ttk.Frame(app, padding="120")
        self.dbEntryFrame.grid(column=0,row=0, sticky=(N, W, E, S))
        self.getUsername = Entry(self.dbEntryFrame)
        self.getUsername.grid(column=0, row=0)
        self.getUsername.bind("<Return>", self.openDatabase)
        self.dbName = ""

        # Mainframe is the opening frame, thats inside the app. Heres our setup
        self.mainframe = ttk.Frame(app, padding="50")
        #mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        CURRENTMONTH = getCurrentMonth()
        self.curMonth = StringVar()
        self.curMonth.set(CURRENTMONTH)

        # If I wanted a label, say for the total costs for the month?
        self.welcomeString = StringVar()
        self.welcomeString.set("View " + CURRENTMONTH + " finances?")
        ttk.Label(self.mainframe, textvariable=self.welcomeString).grid(column=0, row=0)

        # Heres how we can create a Text Entry box that will set the month variable.
        # We set its parent to mainframe, and set where it will appear
        self.month = StringVar()
        # Need an array of months
        monthList = ('January', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        month_entry = ttk.Combobox(self.mainframe, textvariable=self.month, values=monthList, state="readonly")
        #Triggers on any change to 
        month_entry.bind('<<ComboboxSelected>>', self.setMonth)

        self.selectMonth = StringVar()
        self.selectMonth.set("Select " + CURRENTMONTH)
        ttk.Button(self.mainframe, textvariable=self.selectMonth, command=self.tester).grid(column=0, row=4, sticky=(N,E,S,W))

        self.showCostCategory = ttk.Button(self.mainframe, text="Show Cost for Category", command=self.showCostByCategory)
        self.showCostCategory.grid(column=0,row=5)

        # Now lets add a section where we can add our cost obj

        # Cost Input: Entry with validation
        ttk.Label(self.mainframe, text="Add a cost?").grid(column=1, row=0)
        self.lastGoodCostNum = IntVar()
        self.costEntry = ttk.Entry(self.mainframe , validatecommand=self.checkNumeric, validate="focus")
        self.costEntry.grid(column=1,row=1) 
        self.costEntry.bind("<Return>", self.checkNumeric)  

        # Date Input : DateEntry
        ttk.Label(self.mainframe, text="Date of Cost?").grid(column=1, row=2)
        self.costDateEntry = DateEntry(self.mainframe, width= 16, foreground= "white",bd=2)
        self.costDateEntry.grid(column=1,row=3)

        # Category Input : ComboBox
        ttk.Label(self.mainframe, text="Category of Cost?").grid(column=1, row=4)
        self.costCategory = StringVar()
        # Need an array of costs -> TODO: Get from DB and add an entry box to validate
        # costCategories = loadCostCategories()
        costCategories = ('', 'Household', 'Grocery', 'Clothing', 'Dining')
        costCatgeoryEntry = ttk.Combobox(self.mainframe, textvariable=self.costCategory, values=costCategories, state="readonly")
        #Triggers on any change to the box
        costCatgeoryEntry.bind('<<ComboboxSelected>>', self.setCategory)
        costCatgeoryEntry.grid(column=1, row=5)

        self.inputCost = ttk.Button(self.mainframe, text="Submit Cost", state=DISABLED, command=self.enterData)
        self.inputCost.grid(column=1,row=99)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5,pady=5)
        
    
    # Checks a number input through a textbox to make sure it is a number
    def checkNumeric(self, *args):
        try:
            #Still need checking for a comma entry cost eg: 11.50
            costEntryVal = int(self.costEntry.get())
            print(str(costEntryVal) + " is valid")
            self.inputCost['state'] = tk.NORMAL
            return True
        except ValueError:
            print("Value entered wasn't a number")
            self.inputCost['state'] = tk.DISABLED
            return False

    # Checks all the other validation methods to assure values were picked
    def canEnterData(self, *args):
        if(not self.checkNumeric()):
            print("Value was not satisfied")
            return False
        return True

    def enterData(self, *args):
        if(not self.canEnterData()):
            print("Not valid")
        cost = int(self.costEntry.get())
        my_dt = self.costDateEntry.get_date()
        category = self.costCategory.get()

        print("You spent " + str(cost) + " on " + category + " on the date of " + self.costDateEntry.get())
        # Create/Connect to finances.db
        conn = sqlite3.connect('finances.db')
        # Create cursor
        c = conn.cursor()
        # Execute Insert
        c.execute("INSERT INTO costs VALUES (:cost, :spenddate, :category)",
            {
                'cost': cost,
                'spenddate': time.mktime(my_dt.timetuple()),
                'category':category
            }
        )
        conn.commit()
        conn.close()

    def setCategory(self, *args):
        print("Got " + self.costCategory.get())

    # Check if DB exists 
    def openDatabase(self, *args):
        tryUsername = self.getUsername.get()
        if(openDB(tryUsername)):
            # Successfully opened the DB. Set DB string as such
            self.dbName = f'{tryUsername}_finances.db'
            printt(f"Connected to existing database {tryUsername}")
        else:
            #TODD: Add a error box saying that DB does not exist? Would you like to add it
            print("Creating DB for User")
            createDB(tryUsername)
        self.dbEntryFrame.destroy()
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


    # DB QUERY METHOD BUTTONS
    def showCostByCategory(self, *args):
        # Create/Connect to finances.db
        conn = sqlite3.connect(self.dbName)
        # Create cursor
        c = conn.cursor()
        # Execute Insert
        c.execute("SELECT Sum(cost)  FROM COSTS WHERE category = 'Household'")
        records = c.fetchall()
        print(records)
        conn.commit()
        conn.close()

    def tester(self, *args):
        try:
            print("Clicked Button")
        except ValueError:
            pass
    def setMonth(self, *args):
        try:
            CURRENTMONTH = self.month.get()
            self.curMonth.set(CURRENTMONTH)
            self.welcomeString.set("View " + CURRENTMONTH + " finances?")
            self.selectMonth.set("Select " + CURRENTMONTH)
        except ValueError:
            pass

app = Tk()
MasterGUI(app)
app.mainloop()