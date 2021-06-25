#Practical 4

#This code was adapted from the GUI Starter File on Canvas

from tkinter import *

class Application(Frame):

    #Intializing function
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    #Function that will create multiple widgets
    def create_widgets(self):

        #variables that are being set equal to an image to be used later in the code
        self.roman = PhotoImage(file = "roman.gif")
        self.rando = PhotoImage(file = "random.gif")

        #The first label, and its grid point, acts as a header for the GUI
        self.lbl1 = Label(self, text = "Roman Numeral Canvas")
        self.lbl1.grid(row = 0, column = 1, columnspan = 2)

        #The canvas and, its grid points
        self.canvas = Canvas(self, height = 310, width = 500)
        self.canvas.grid(row = 1, column = 0, columnspan = 2, rowspan = 5)

        #The second label and, its grid point, acts as an option for user response
        self.lbl2 = Label(self, text = "Number:")
        self.lbl2.grid(row = 1, column = 2, sticky = W)

        #Entry box for the user to input a number
        self.ent = Entry(self, width = 30)
        self.ent.grid(row = 1, column = 3, sticky = W)

        #Check Box for the user to indicate multiple numbers
        self.numbers = BooleanVar()
        Checkbutton(self, text = "Numbers", variable = self.numbers).grid(row = 1, column = 4, columnspan = 2)

        #The third label and, its grid point 
        self.lbl3 = Label(self, text = "Line Width:")
        self.lbl3.grid(row = 2, column = 2, sticky = W)

        #Radio Buttons for the user to select different lengths of line width
        self.width = StringVar()
        self.width.set("1")
        Radiobutton(self, text = "1", variable = self.width, value = "1").grid(row = 2, column = 3, columnspan = 1)
        Radiobutton(self, text = "3", variable = self.width, value = "3").grid(row = 2, column = 4, columnspan = 1)
        Radiobutton(self, text = "5", variable = self.width, value = "5").grid(row = 2, column = 5, columnspan = 1)
        
        #The Fourth label and, its grid point
        self.lbl4 = Label(self, text = "Line Color:")
        self.lbl4.grid(row = 3, column = 2, sticky = W)

        #Radio Buttons for the user to select different colors for their lines
        self.color = StringVar()
        self.color.set("black")
        Radiobutton(self, text = "Black", variable = self.color, value = "black").grid(row = 3, column = 3, columnspan = 1)
        Radiobutton(self, text = "Red", variable = self.color, value = "red").grid(row = 3, column = 4, columnspan = 1)
        Radiobutton(self, text = "Blue", variable = self.color, value = "blue").grid(row = 3, column = 5, columnspan = 1)

        #The first button which is a photo image plus its grid point
        self.bttn1 = Button(self, image = self.roman, command = self.run)
        self.bttn1.grid(row = 4, column = 3, sticky = W)

        #The second button which is also a photo image plus its grid point 
        self.bttn2 = Button(self, image = self.rando, command = self.run)
        self.bttn2.grid(row = 4, column = 4, columnspan = 2, rowspan = 1)

        #Starting point for the pen, and the width of each line
        self.x, self.y = 20, 20
        
    #Function that is called upon with the buttons, that will call the separate functions specefied by numerals the user selects
    def run(self):
        num = ""
        

        #If else statement that adds the user's input to an empty string so that each letter drawn is different
        if self.numbers == True:
            num += self.ent.get().upper()
        else:
            num += self.ent.get().upper()

        #If statements that test to see which letter the user has inputted so that it can be drawn
        if "M" in num:
            print("M")

        if "X" in num:
            print("X")

        if "D" in num:
            print("D")

        if "C" in num:
            print("C")

        if "L" in num:
            print("L")

        if "V" in num:
            print("V")

        if "I" in num:
            #This will draw the letter each time the button is pressed no matter its position
            x1, y1 = self.x, self.y
            x2, y2 = self.x + 10, self.y
            x3, y3 = self.x + 20, self.y
            x4, y4 = self.x + 10, self.y + 40
            x5, y5 = self.x + 10, self.y + 40
            x6, y6 = self.x, self.y + 40
            x7, y7 = self.x + 20, self.y + 40

            #Drawing the lines of the I numeral, the user can change the color and width of the letter by the radio buttons that are created in the beginning
            self.canvas.create_line(x1, y1, x2, y2, fill = self.color.get(), width = int(self.width.get()))
            self.canvas.create_line(x2, y2, x3, y3, fill = self.color.get(), width = int(self.width.get()))
            self.canvas.create_line(x3, y3, x2, y2, fill = self.color.get(), width = int(self.width.get()))
            self.canvas.create_line(x2, y2, x4, y4, fill = self.color.get(), width = int(self.width.get()))
            self.canvas.create_line(x4, y4, x5, y5, fill = self.color.get(), width = int(self.width.get()))
            self.canvas.create_line(x5, y5, x6, y6, fill = self.color.get(), width = int(self.width.get()))
            self.canvas.create_line(x6, y6, x7, y7, fill = self.color.get(), width = int(self.width.get()))

            #This will offset each letter by the amount of pixels necessary since they are always 20 wide it must be 30 pixels to get the correct distance
            self.x = self.x + 30
            
# main
root = Tk()
root.title("Roman Numerals")
root.geometry("900x350")


app = Application(root)
root.mainloop()

#I ran out of time to do all of the drawing for all of the other letters but, /
#I was able to code at least one letter that is able to change colors and width
