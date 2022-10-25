from tkinter import *
from tkinter import ttk
from random import *
# Create Object
root = Tk()
# Set geometry
root.geometry("500x500")
root.title("Rock-Paper-Scissors-Game")
# List of players
list = ["rock","paper","scissors"]
choose_number = randint(0,2)
print(choose_number) # For testing if it works
label = Label(root,text="select your choice",width = 20,height=4,font=("calibri",15))
label.pack()
