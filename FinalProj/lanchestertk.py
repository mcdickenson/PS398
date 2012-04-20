#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/
# The Lanchester Squares Game

# load packages
from Tkinter import *

periodLabels = ['1', '2', '3', '4', '5', 'Total']

class LanchesterSquares:
    def __init__(self, myParent):   # this is where I initialize the game
        self.myContainer1 = Frame(myParent)
        self.myContainer1.grid()
        self.start()                # sets all starting variables
        self.makeLayout()           # makes the frame layout

    def start(self):
        self.currentTextOut = "Welcome to the Lanchester Squares Game"

    def makeLayout(self): # makes basic layout, with optional title: 
        self.mainLabel = Label(self.myContainer1, font=('Helvetica',24), text = 'Lanchester Squares', fg='blue')
        self.mainLabel.grid(row=0, column=0, columnspan=9, sticky=N)
        # make sure that columnspan is the width of the whole frame

        # make text labels
        self.periodLabel = Label(self.myContainer1, font=('Helvetica',14), text = 'Time Period', fg='black')
        self.periodLabel.grid(row=3, column=5, sticky=N)

        self.troopsLabel = Label(self.myContainer1, font=('Helvetica',14), text = 'Troops', fg='black')
        self.troopsLabel.grid(row=3, column=6, sticky=N)

        self.investLabel = Label(self.myContainer1, font=('Helvetica',14), text = 'Investment $', fg='black')
        self.investLabel.grid(row=3, column=7, sticky=N)

        self.turnLabel = Label(self.myContainer1, font=('Helvetica',18), text = "It is __'s turn", fg='black')
        self.turnLabel.grid(row=20, column=6, columnspan=3, sticky=W)

        self.blankLabel = Label(self.myContainer1, text='      ') 
        #self.blankLabel.grid(row=1, column=4) # a blank column
        self.blankLabel.grid(row=1, column=8)
        #self.blankLabel.grid(row=1, columnspan=8, sticky=N) # a blank row

        # make time period labels
        self.labelDict = {}
        for rowNum in range(0,6):
            self.labelDict[rowNum] = Label(self.myContainer1, text=periodLabels[rowNum])
            self.labelDict[rowNum].grid(row=rowNum+4, column=5, sticky=N)

        # make entry boxes
        self.troopInputDict = {}
        self.investInputDict = {}
        for rowNum in range(0,5):
            self.troopInputDict[rowNum] = Entry(self.myContainer1, width=4, bg='white', fg='black', font=('Helvetica', 14))
            self.troopInputDict[rowNum].grid(row=rowNum+4, column=6, sticky=N)
            self.investInputDict[rowNum] = Entry(self.myContainer1, width=4, bg='white', fg='black', font=('Helvetica', 14))
            self.investInputDict[rowNum].grid(row=rowNum+4, column=7, sticky=N)
            
        # make buttons
        self.simulateButton = Button(self.myContainer1, text='Simulate', width=9, height=1, command=lambda: self.pressSimulate())
        self.simulateButton.grid(row=23, column=2)

        self.enterButton = Button(self.myContainer1, text='Enter', width=6, height=1, command=lambda: self.pressEnter())
        self.enterButton.grid(row=10, column=6)

        # make starting photo
        startPhoto = PhotoImage(file='lanchester1.gif')
        self.photoLabel = Label(self.myContainer1, image=startPhoto)
        self.photoLabel.image = startPhoto
        self.photoLabel.grid(row=2, column=1, rowspan=20,columnspan=3, sticky=W)
        

    def pressSimulate(self):
        simPhoto = PhotoImage(file='lanchTester2.gif')
        self.photoLabel = Label(self.myContainer1, image=simPhoto)
        self.photoLabel.image = simPhoto
        self.photoLabel.grid(row=2, column=1, rowspan=20,columnspan=3, sticky=W)

        #TODO: find a standard resolution for files to include
        #TODO: create a blank image of that size - axes limits should be maximum forces allowed
        #TODO: work on importing png files http://effbot.org/tkinterbook/photoimage.htm, http://www.pythonware.com/library/pil/handbook/image.htm

    def pressEnter(self):
        pass

    
         

# initialize the game
root = Tk()
root.geometry('1100x700+150+20')    # size and position of the game window; width, height, w.offset, h.offset
mygame = LanchesterSquares(root)    # place elements in window
root.title('Lanchester Squares')    # window title
root.mainloop()                     # start the game

