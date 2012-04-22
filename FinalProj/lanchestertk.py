#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/
# The Lanchester Squares Game

# load packages
from PIL import Image as pilImage
from PIL import ImageTk as pilImageTk
#from PIL import Image, ImageTk # as pilImage, ImageTk as pilImageTk
from Tkinter import *

import locale
locale.setlocale(locale.LC_ALL, "")

periodLabels = ['10', '20', '30', '40', '50', 'Subtotal', 'Total']
# TODO: add csv writing functionality to record player actions


class LanchesterSquares:
    def __init__(self, myParent):   # this is where I initialize the game
        self.myContainer1 = Frame(myParent)
        self.myContainer1.grid()
        self.start()                # sets all starting variables
        self.makeLayout()           # makes the frame layout

    def start(self):
        self.currentTextOut = "Welcome to the Lanchester Squares Game"
        self.currentPlayer = 1
        self.playerNames = ['', '', '']
        self.troopDeployments = ['', [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.investment = [0, 0, 0]
        self.totalTroops = [0, 0, 0]
        self.allowEnter = False
        self.allowSimulate = False

    def makeLayout(self): # makes basic layout, with optional title: 
        self.mainLabel = Label(self.myContainer1, font=('Helvetica',24), text = 'Lanchester Squares', fg='blue')
        self.mainLabel.grid(row=0, column=0, columnspan=9, sticky=N)
        # make sure that columnspan is the width of the whole frame

        # make text labels
        self.periodLabel = Label(self.myContainer1, font=('Helvetica',14), text = 'Time Period', fg='black')
        self.periodLabel.grid(row=13, column=5, sticky=N)

        self.troopsLabel = Label(self.myContainer1, font=('Helvetica',14), text = 'Troops (k)', fg='black')
        self.troopsLabel.grid(row=13, column=6, sticky=N)

        self.investLabel = Label(self.myContainer1, font=('Helvetica',14), text = 'Investment ($m)', fg='black')
        self.investLabel.grid(row=13, column=7, sticky=N)

        self.blankLabel = Label(self.myContainer1, text='      ') 
        #self.blankLabel.grid(row=1, column=4) # a blank column
        self.blankLabel.grid(row=1, column=8)
        #self.blankLabel.grid(row=1, columnspan=8, sticky=N) # a blank row

        # make time period labels
        self.labelDict = {}
        for rowNum in range(0,7):
            self.labelDict[rowNum] = Label(self.myContainer1, text=periodLabels[rowNum])
            self.labelDict[rowNum].grid(row=rowNum+14, column=5, sticky=N)

        # make entry boxes
        self.troopInputDict = {}
        self.investInputDict = {}
        for rowNum in range(0,5):
            self.troopInputDict[rowNum] = Entry(self.myContainer1, width=4, bg='white', fg='black', font=('Helvetica', 14))
            self.troopInputDict[rowNum].grid(row=rowNum+14, column=6, sticky=N)
        for rowNum in range(0,1):
            self.investInputDict[rowNum] = Entry(self.myContainer1, width=4, bg='white', fg='black', font=('Helvetica', 14))
            self.investInputDict[rowNum].grid(row=rowNum+14, column=7, sticky=N)
            
        # make buttons
        self.simulateButton = Button(self.myContainer1, text='Simulate', width=9, height=1, command=lambda: self.pressSimulate())
        self.simulateButton.grid(row=23, column=2)

        self.enterButton = Button(self.myContainer1, text='Enter', width=6, height=1, command=lambda: self.enterStrategy())
        self.enterButton.grid(row=23, column=6)

        # make starting photo
        startPhoto = PhotoImage(file='reinfTester.gif')
        self.photoLabel = Label(self.myContainer1, image=startPhoto)
        self.photoLabel.image = startPhoto
        self.photoLabel.grid(row=2, column=1, rowspan=20,columnspan=3, sticky=W)

        # set starting text
        self.makeText('getPlayerName')

    def makeText(self, whatToDo):
        if whatToDo == 'getPlayerName':
            textOut = "Player " + str(self.currentPlayer) + ", what is your name?"
            
            self.nameBox = Entry(self.myContainer1, width = 12, bg='white', fg='black', font=('Helvetica', 14))
            self.nameBox.grid(row=4, column=5, columnspan=2, sticky=N)
            self.nameButton = Button(self.myContainer1, text='Set', width=4, height=1, command=lambda: self.enterName())
            self.nameButton.grid(row=4, column=7, sticky=N)

        elif whatToDo == 'getStrategy':
            self.turnLabel.grid_forget()
            textOut = self.playerNames[self.currentPlayer] + ", enter your strategy."
            self.allowEnter = True
            
        else: 
            textOut = "It is player " + str(self.currentPlayer) +"'s turn."
            
        self.turnLabel = Label(self.myContainer1, font=('Helvetica',18), text = textOut, fg='black')
        self.turnLabel.grid(row=3, column=5, columnspan=3, sticky=N)

    def pressSimulate(self):
        if self.allowSimulate:
            simPhoto = PhotoImage(file='lanchTester2.gif')
            self.photoLabel = Label(self.myContainer1, image=simPhoto)
            self.photoLabel.image = simPhoto
            self.photoLabel.grid(row=2, column=1, rowspan=20,columnspan=3, sticky=W)
        else:
            pass

        #TODO: find a standard resolution for files to include
        #TODO: create a blank image of that size - axes limits should be maximum forces allowed
        #TODO: work on importing png files http://effbot.org/tkinterbook/photoimage.htm, http://www.pythonware.com/library/pil/handbook/image.htm

    def enterStrategy(self): # TODO: make this only accept numbers greater than 0 and with total less than constraints
                             # TODO: and make sure strings aren't passed
        if self.allowEnter:
            for period in range(0,5): # get troop counts from input boxes
                temp = self.troopInputDict[period].get()
                self.troopDeployments[self.currentPlayer][period] = float(temp)
            self.totalTroops[self.currentPlayer] = sum(self.troopDeployments[self.currentPlayer])

            # get player's $ invested
            self.investment[self.currentPlayer] = float(self.investInputDict[0].get())
            tempInvestment = self.investment[self.currentPlayer]*1000000
            tempInvestment = "$" + locale.format('%0.2f', tempInvestment, True)

            # calculate grand total spending
            grandTotal = self.totalTroops[self.currentPlayer] * 20000 + self.investment[self.currentPlayer] * 1000000
            grandTotal = "$" + locale.format('%0.2f', grandTotal, True)
            
            # display player's total number of troops and investment
            self.troopLabel = Label(self.myContainer1, font=('Helvetica',14), text = str(self.totalTroops[self.currentPlayer]), fg='black')
            self.troopLabel.grid(row=19, column=6, sticky=N)
            
            self.investLabel = Label(self.myContainer1, font=('Helvetica',14), text = tempInvestment, fg='black')
            self.investLabel.grid(row=19, column=7, sticky=N)

            self.grandTotalLabel = Label(self.myContainer1, font=('Helvetica',14), text = grandTotal, fg='black')
            self.grandTotalLabel.grid(row=20, column=7, sticky=N)
            
        else:
            pass

    def enterName(self):
        self.playerNames[self.currentPlayer] = self.nameBox.get()[0:12] # maximum name length = 12

        if self.currentPlayer == 1:
            self.currentPlayer = 2
            self.nameBox.grid_forget()
            self.nameButton.grid_forget()
            self.turnLabel.grid_forget()
            self.makeText('getPlayerName')
            
        elif self.currentPlayer == 2:
            self.currentPlayer = 1
            self.nameBox.grid_forget()
            self.nameButton.grid_forget()
            self.makeText('getStrategy')
         

# initialize the game
root = Tk()
root.geometry('1100x700+150+20')    # size and position of the game window; width, height, w.offset, h.offset
mygame = LanchesterSquares(root)    # place elements in window
root.title('Lanchester Squares')    # window title
root.mainloop()                     # start the game

