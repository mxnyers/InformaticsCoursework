#9.20

#This section of code imports the different functons needed to complete a random choice and to create a successful GUI
from tkinter import *

import random

#Supreeth helped me figure out how to setup my random choice and how to bind code, the rest I adapted from lecture slides 25-27 or from my own knowledge
from tkinter.messagebox import showinfo

#Class that will become a GUI
class Guess_Game(Frame):

#An initializing function that will also select a random number for the user to guess
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.correct = random.choice(self.num_list)
        print(self.correct)

#Function that creates widgets and labels, that are grided into the GUI
    def create_widgets(self):
        self.lbl = Label(self, text = "Enter your guess:")
        self.lbl.grid(row = 0, column = 0, sticky = W)
        self.answer = Entry(self)
        self.answer.grid(row = 1, column = 0, sticky = W)
        self.bttn1 = Button(self, text = "Enter", command = self.play)
        self.bttn1.grid(row = 2, column = 0, columnspan = 2)

#9.21
#Binding method that makes the answer appear just as the button does
        self.answer.bind("<Return>", self.play)

#Function that calls upon the enter/return key to run the program and tests to see if the user guessed the correct number
    def play(self, event):
        print(self.answer.get())
        if int(self.answer.get()) == self.correct:
            showinfo(message = "That is Correct! \n Lets do this again...")

#9.22
#This part of the function resets the game so the user can play over and over again
            self.correct = random.choice(self.num_list)
            print(self.correct)
        else:
            showinfo(message = "That is not correct, guess again!")
#main
root = Tk()
root.title("tk")
root.geometry("10x75")
app = Guess_Game(root)
root.mainloop()



#Additional Problem

class Robot_Delivery(Frame):

#initializing function
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        

    def create_widgets(self):
        #Row 1 code that allows a user response
        self.lbl1 = Label(self, text = "What would you like delivered?")
        self.lbl1.grid(row = 0, column = 0, sticky = W)
        self.item = Entry(self, width = 60)
        self.item.grid(row = 0, column = 1, columnspan = 3)

        #Row 2 code that lets the user know that there are options
        self.lbl2 = Label(self, text = "Options")
        self.lbl2.grid(row = 1, column = 2, sticky = W)

        #Delivery Method code that begins with a title and options represented with radio buttons
        self.lbl3 = Label(self, text = "Delivery Method:")
        self.lbl3.grid(row = 2, column = 0, columnspan = 1)

        self.method = StringVar()
        self.method.set("Flying Drone")

        Radiobutton(self, text = "Flying Drone ($10)", variable = self.method, value = "Flying Drone").grid(row = 3, column = 0, columnspan = 1)
        Radiobutton(self, text = "Self Driving Car ($20)", variable = self.method, value = "Self Driving Car").grid(row = 4, column = 0, columnspan = 1)
        Radiobutton(self, text = "Giant Robot ($1000)", variable = self.method, value = "Giant Robot").grid(row = 5, column = 0, columnspan = 1)

        #Addons code that begins with a title and options represented with check buttons
        self.lbl4 = Label(self, text = "Addons:")
        self.lbl4.grid(row = 2, column = 3, columnspan = 1)

        self.deliver = BooleanVar()
        self.broken = BooleanVar()
        self.smile = BooleanVar()

        Checkbutton(self, text = "Express Delivery (+$30)", variable = self.deliver).grid(row = 3, column = 3, columnspan = 1)
        Checkbutton(self, text = "Mostly Not Broken (+$20)", variable = self.broken).grid(row = 4, column = 3, columnspan = 1)
        Checkbutton(self, text="With a Smile (+$1)", variable = self.smile).grid(row = 5, column = 3, columnspan = 1)

        #The confirm delivery button which will run the delivery system
        self.bttn = Button(self, text = "Confirm Delivery", command = self.response)
        self.bttn.grid(row = 6, column = 2, columnspan = 1)

        #Text box that reviews the order with the customer
        self.results_txt = Text(self, width = 70, height = 4, wrap = WORD)
        self.results_txt.grid(row = 7, column=0, columnspan = 4)

#Function that responds to the user with a recap on everything they had just clicked
    def response(self):
        info = "You have selected to have a " + self.item.get() + " delivered by a " + self.method.get() +  " with "  

        addon = []
        cost = 0

#If and else statements that add on to the response and add up the total cost with all the add ons they may purchase
        if self.deliver.get():
            addon.append("express delivery")
            cost += 30

        if self.broken.get():
            addon.append("mostly not broken")
            cost += 20

        if self.smile.get():
            addon.append("with a smile")
            cost += 1

        if self.method.get() == "Flying Drone":
            cost += 10

        if self.method.get() == "Self Driving Car":
            cost += 20

        if self.method.get() == "Giant Robot":
            cost += 1000

        if len(addon) > 0:
            addon = ", ".join(addon)
            info += addon + "."
            info += " Your total delivery fee comes to: $" + str(cost)

        else:
            info += "no add-ons"
            info += " Your total delivery fee comes to: $" + str(cost)
            
        
# This resets the response so that the user can do this multiple times if they would want to        
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, info)
    


#main
root = Tk()
root.title("Robot Delivery System")
root.geometry("560x250")
app = Robot_Delivery(root)
root.mainloop()
        
