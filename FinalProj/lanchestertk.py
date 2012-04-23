#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/
# The Lanchester Squares Game

# load packages
from Tkinter import *
import slopefieldPlot as sp # my script for plotting slope fields
import pngToGif as ptg # my script for converting png to gif
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
        self.makeText('getPlayerName') # set starting text

    def start(self):
        self.currentTextOut = "Welcome to the Lanchester Squares Game"
        self.currentPlayer = 1
        self.playerNames = ['', '', '']
        self.troopDeployments = ['', [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.investment = [0, 0, 0]
        self.totalTroops = [0, 0, 0]
        self.allowEnter = False
        self.allowSimulate = False
        self.maxResource = 1000000000 # maximum resources, in dollars

    def makeLayout(self): # makes basic layout, with optional title
        self.mainLabel = Label(self.myContainer1, font=('Helvetica',24), text = 'Lanchester Squares', fg='blue')
        self.mainLabel.grid(row=0, column=0, columnspan=9, sticky=N+E+S+W)
        # make sure that columnspan is the width of the whole frame

        # make text labels
        self.periodLabel = Label(self.myContainer1, font=('Helvetica',14), text = 'Time Period', fg='black')
        self.periodLabel.grid(row=13, column=5, sticky=N+E+S+W)

        self.troopsLabel = Label(self.myContainer1, font=('Helvetica',14), text = 'Troops (10k)', fg='black')
        self.troopsLabel.grid(row=13, column=6, sticky=N+E+S+W)

        self.investLabel = Label(self.myContainer1, font=('Helvetica',14), text = 'Investment ($m)', fg='black')
        self.investLabel.grid(row=13, column=7, sticky=N+E+S+W)

        self.blankLabel = Label(self.myContainer1, text='      ') 
        self.blankLabel.grid(row=1, column=8)

        # make time period labels
        self.labelDict = {}
        for rowNum in range(0,7):
            self.labelDict[rowNum] = Label(self.myContainer1, text=periodLabels[rowNum])
            self.labelDict[rowNum].grid(row=rowNum+14, column=5, sticky=N+E+S+W)

        # make entry boxes
        self.troopInputDict = {}
        self.investInputDict = {}
        for rowNum in range(0,5):
            self.troopInputDict[rowNum] = Entry(self.myContainer1, width=4, bg='white', fg='black', font=('Helvetica', 14))
            self.troopInputDict[rowNum].grid(row=rowNum+14, column=6, sticky=E+W)
        for rowNum in range(0,1):
            self.investInputDict[rowNum] = Entry(self.myContainer1, width=4, bg='white', fg='black', font=('Helvetica', 14))
            self.investInputDict[rowNum].grid(row=rowNum+14, column=7, sticky=E)
            
        # make buttons
        self.simulateButton = Button(self.myContainer1, text='Simulate', width=9, height=1, command=lambda: self.pressSimulate())
        self.simulateButton.grid(row=23, column=2)

        self.enterButton = Button(self.myContainer1, text='Enter', width=6, height=1, command=lambda: self.enterStrategy())
        self.enterButton.grid(row=23, column=6)

        # make starting photo
        startPhoto = PhotoImage(file='reinfTester.gif')
        self.photoLabel = Label(self.myContainer1, image=startPhoto)
        self.photoLabel.image = startPhoto
        self.photoLabel.grid(row=2, column=1, rowspan=20,columnspan=3, sticky=W+E)

    def makeText(self, whatToDo):
        if whatToDo == 'getPlayerName':
            textOut = "Player " + str(self.currentPlayer) + ", what is your name?"
            
            self.nameBox = Entry(self.myContainer1, width = 12, bg='white', fg='black', font=('Helvetica', 14))
            self.nameBox.grid(row=4, column=5, columnspan=2, sticky=N+E+W)
            self.nameButton = Button(self.myContainer1, text='Set', width=4, height=1, command=lambda: self.enterName())
            self.nameButton.grid(row=4, column=7, sticky=N)

        elif whatToDo == 'getStrategy':
            self.turnLabel.grid_forget()
            textOut = self.playerNames[self.currentPlayer] + ", enter your strategy."
            self.allowEnter = True
            
        else: 
            textOut = "It is player " + str(self.currentPlayer) +"'s turn."
            
        self.turnLabel = Label(self.myContainer1, font=('Helvetica',18), text = textOut, fg='black')
        self.turnLabel.grid(row=3, column=5, columnspan=4, sticky=N+S+W)

    def enterStrategy(self): # TODO: make this only accept numbers greater than 0
                             # TODO: and make sure strings aren't passed (raises a ValueError)
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
            grandTotal = self.totalTroops[self.currentPlayer] * 200000000 + self.investment[self.currentPlayer] * 1000000
            grandTotalStr = "$" + locale.format('%0.2f', grandTotal, True)
            
            # display player's total number of troops and investment
            self.troopLabel = Label(self.myContainer1, font=('Helvetica',14), text = str(self.totalTroops[self.currentPlayer]), fg='black')
            self.troopLabel.grid(row=19, column=6, sticky=N+E+S+W)
            
            self.investmentLabel = Label(self.myContainer1, font=('Helvetica',14), text = tempInvestment, fg='black')
            self.investmentLabel.grid(row=19, column=7, sticky=N+E+S+W)

            self.grandTotalLabel = Label(self.myContainer1, font=('Helvetica',14), text = grandTotalStr, fg='black')
            self.grandTotalLabel.grid(row=20, column=7, sticky=N+E+S+W)

            # check for forbidden input
            if grandTotal > self.maxResource:
                self.popupError("You have exceeded your total resources.\nPlease re-enter.")

            elif grandTotal < self.maxResource*0.9:
                self.popupError("You are using less than 90 percent of\n your total resources. Please re-enter.")

            elif self.currentPlayer == 1:
                self.makeLayout() # clear unneeded text
                self.troopLabel.grid_forget()
                self.investmentLabel.grid_forget()
                self.grandTotalLabel.grid_forget()
                self.currentPlayer = 2
                self.makeText('getStrategy') # get player 2's strategy

            elif self.currentPlayer == 2:
                self.derivDenominator = 10 * (self.investment[1] + self.investment[2] + 1)
                self.dy = -self.investment[1] / self.derivDenominator
                self.dx = -self.investment[2] / self.derivDenominator
                self.allowSimulate = True
                # TODO: make sure players know they now need to click "Simulate"
            
        else:
            pass

    def popupError(self, messageText):
        self.top = Toplevel()
        self.top.title("Error")
        self.top.geometry('300x170+830+400')

        msg = Label(self.top, text=messageText)
        msg.grid(row=1, column=0, columnspan=3, rowspan=3)

        errButton = Button(self.top, text="OK", command=lambda: self.clearError())
        errButton.grid(row=4, column=1)

    def clearError(self):
        self.troopLabel.grid_forget()
        self.investmentLabel.grid_forget()
        self.grandTotalLabel.grid_forget()
        self.top.destroy()
        
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

    def pressSimulate(self):
        outputName = 'simTester1'
        #outputName = str(datetime.now())[0:10]
        if self.allowSimulate:
            # create slopefield plot
            sp.slopefieldPlotter(0, self.totalTroops[1], .2,
                                             0, self.totalTroops[2], .2, self.dx, self.dy,
                                             xLab=self.playerNames[1], yLab=self.playerNames[2],
                mainLab='', drawAxes=True, filename=outputName)

            # draw vectors and arrows
            x_temp, y_temp = 0, 0
            for p in range(0,5):
                # vectors
                sp.drawVector(0, self.dx, self.dy, 0,
                                      x_temp+self.troopDeployments[1][p], y_temp+self.troopDeployments[2][p],
                                      100, 0.1) # num steps and stepsize

                # find ending point of vector (as starting point for arrows)
                x_temp, y_temp = sp.getEndVector(0, self.dx, self.dy, 0,
                                      self.troopDeployments[1][p], self.troopDeployments[2][p],
                                      100, 0.1)
                # arrows
                if p < 4:
                    if (self.troopDeployments[1][p+1] > 0) & (self.troopDeployments[2][p+1] <= 0): # or p
                        sp.drawArrow(x_temp, x_temp+self.troopDeployments[1][p+1], y_temp, y_temp, headlength=0.05, direction='R', lineColor='r')
                        
                    if (self.troopDeployments[2][p+1] > 0) & (self.troopDeployments[1][p+1] <= 0):
                        sp.drawArrow(x_temp, x_temp, y_temp, y_temp+self.troopDeployments[2][p+1], headlength=0.05, direction='U', lineColor='r')
                        
                    if (self.troopDeployments[1][p+1] > 0) & (self.troopDeployments[2][p+1] > 0):
                        sp.drawArrow(x_temp, x_temp+self.troopDeployments[1][p+1], y_temp, y_temp, headlength=0.05, direction='R', lineColor='r')
                        sp.drawArrow(x_temp+self.troopDeployments[1][p+1], x_temp+self.troopDeployments[1][p+1],
                                     y_temp, y_temp+self.troopDeployments[2][p+1], headlength=0.05, direction='U', lineColor='r')

            sp.drawFinalVector(0, self.dx, self.dy, 0, x_temp, y_temp)
                # TODO: add filename parameter
                # TODO: rescale arrows
                # TODO: rescale investment input
 
            #save file and convert to gif
            sp.pngSave(outputName)
            ptg.pngToGif(outputName)
            
            simPhoto = PhotoImage(file=outputName+'.gif')
            self.photoLabel = Label(self.myContainer1, image=simPhoto)
            self.photoLabel.image = simPhoto
            self.photoLabel.grid(row=2, column=1, rowspan=20,columnspan=3, sticky=W)
        else:
            pass

        #TODO: find a standard resolution for files to include
        #TODO: create a blank image of that size - axes limits should be maximum forces allowed
         

# initialize the game
root = Tk()
root.geometry('1100x700+150+40')    # size and position of the game window; width, height, w.offset, h.offset
mygame = LanchesterSquares(root)    # place elements in window
root.title('Lanchester Squares')    # window title
root.mainloop()                     # start the game

#TODO: call slopefieldPlot with player inputs, current time as filename
#TODO: add a different default plot, possibly including instructions
#TODO: write player input to CSV
#TODO: popup announcing who won, at what time, and with how many troops
#TODO: make it easy to begin another round
