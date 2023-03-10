from helpers.nameHandler import *
from tkinter import *
from tkinter import tkk

# Need to load our data first. From an excel file
# The format of our excel sheet is : 
# Each Col Represents a Week of income. We need to determine this first. 

# Firstly need to make my weekly income to track it

welcomeString = "View " + getCurrentMonth() + " finances?"

# Setup initial dark-mode variables
customtkinter.set_appearance_mode("Dark"); 
customtkinter.set_default_color_theme("dark-blue")

def selectMonth():
    print("Selected this month")