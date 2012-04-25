#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/
# The Lanchester Squares Game

# load packages
from Tkinter import *
import slopefieldPlot as sp # my script for plotting slope fields
import pngToGif as ptg # my script for converting png to gif
import locale, csv, datetime, tkMessageBox
locale.setlocale(locale.LC_ALL, "")

periodLabels = ['10', '20', '30', '40', '50', 'Subtotal', 'Total']

class LanchesterSquares:
    def __init__(self, myParent):   # this is where I initialize the game
        self.myContainer1 = Frame(myParent)
        self.myContainer1.grid()
        self.start()                # sets all starting variables
        self.makeLayout()           # makes the frame layout
        self.makeStartPhoto()       # sets a default start photo
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
        self.maxResource = 1000000000 # maximum resources alotted to players, in "dollars"
        # create csv output file
        Headers = ["p1name", "p2name", "p1deploy1", "p1deploy2", "p1deploy3", "p1deploy4", "p1deploy5", "p1invest", "p2deploy1", "p2deploy2", "p2deploy3", "p2deploy4", "p2deploy5", "p2invest", "pWin", "pLose", "winnerTroops", "battlePeriods", "gametime"]
        nameOutput = "LanchesterSim.csv"
        self.outputFile = open(nameOutput,"wb")
        self.csvwriter = csv.writer(self.outputFile)
        self.csvwriter.writerow(Headers)

    def makeLayout(self): # makes basic layout, with optional title
        self.mainLabel = Label(self.myContainer1, font=('Helvetica',24), text = 'The Lanchester Squares Game', fg='blue')
        self.mainLabel.grid(row=0, column=0, columnspan=9, sticky=N+E+S+W) # make sure that columnspan is the width of the whole frame

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

    def makeStartPhoto(self): # make starting photo
        startPhoto = PhotoImage(file='reinfTester5.gif')
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

        elif whatToDo == 'getSimulation':
            self.turnLabel.grid_forget()
            textOut = "Now press the Simulate button."
            self.allowEnter = False
            self.allowSimulate = True
            
        else: 
            textOut = "It is player " + str(self.currentPlayer) +"'s turn."
            
        self.turnLabel = Label(self.myContainer1, font=('Helvetica',18), text = textOut, fg='black')
        self.turnLabel.grid(row=3, column=5, columnspan=4, sticky=N+S+W)

    def enterStrategy(self): 
        if self.allowEnter:
            try:
                for period in range(0,5): # get troop counts from input boxes
                    temp = self.troopInputDict[period].get()
                    self.troopDeployments[self.currentPlayer][period] = float(temp)
                    if self.troopDeployments[self.currentPlayer][period] < 0:
                        raise ValueError('Negative input')
                
                self.totalTroops[self.currentPlayer] = sum(self.troopDeployments[self.currentPlayer])

                # get player's $ invested
                self.investment[self.currentPlayer] = float(self.investInputDict[0].get())
                if self.investment[self.currentPlayer] < 0 :
                    raise ValueError('Negative input')
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

            except ValueError:
                self.popupError2("Only non-negative numbers are allowed.\nAll cells must contain a value.", False)

            # check for forbidden input
            if grandTotal > self.maxResource:
                self.popupError("You have exceeded your total resources.\nPlease re-enter.", True)

            elif grandTotal < self.maxResource*0.9:
                self.popupError("You are using less than 90 percent of\n your total resources. Please re-enter.", True)

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
                self.makeLayout() # clear unneeded text
                self.troopLabel.grid_forget()
                self.investmentLabel.grid_forget()
                self.grandTotalLabel.grid_forget()
                self.gameTime = str(datetime.datetime.now())
                self.makeText('getSimulation')
            
        else:
            pass

    def popupError(self, messageText, labelsExist=False): # error message for when players enter bad input
        self.top = Toplevel()
        self.top.title("Error")
        self.top.geometry('300x170+830+400')

        msg = Label(self.top, text=messageText)
        msg.grid(row=1, column=0, columnspan=3, rowspan=3)

        if labelsExist:
            errButton = Button(self.top, text="OK", command=lambda: self.clearError())
        else:
            errButton = Button(self.top, text="OK", command=lambda: self.top.destroy())
        errButton.grid(row=4, column=1)

    def clearError(self): # clear player input after they have committed and acknowledged an input error
        self.troopLabel.grid_forget()
        self.investmentLabel.grid_forget()
        self.grandTotalLabel.grid_forget()
        self.top.destroy()
        
    def enterName(self): # function by which players enter their names
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
        #outputName = 'simTester1'
        outputName = self.gameTime
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

                # see if one player has won yet
                xfinal, yfinal, numsteps = sp.getFinalCoord(0, self.dx, self.dy, 0,
                                      x_temp+self.troopDeployments[1][p], y_temp+self.troopDeployments[2][p], 1000)
                if (xfinal <=0) | (yfinal <=0): 
                    self.getWinner(xfinal, yfinal, numsteps)
                    x_temp, y_temp = sp.getEndVector(0, self.dx, self.dy, 0,
                                      x_temp+self.troopDeployments[1][p], y_temp+self.troopDeployments[2][p],
                                      100, 0.1)
                    break

                # find ending point of vector (as starting point for arrows)
                x_temp, y_temp = sp.getEndVector(0, self.dx, self.dy, 0,
                                      x_temp+self.troopDeployments[1][p], y_temp+self.troopDeployments[2][p],
                                      100, 0.1)
                
                # arrows
                if p < 4:
                    thresh = .2 # set threshold for when to draw arrows
                    if (self.troopDeployments[1][p+1] > thresh) & (self.troopDeployments[2][p+1] <= thresh): # or p
                        sp.drawArrow(x_temp, x_temp+self.troopDeployments[1][p+1], y_temp, y_temp, headlength=0.05, direction='R', lineColor='r')
                        
                    if (self.troopDeployments[2][p+1] > thresh) & (self.troopDeployments[1][p+1] <= thresh):
                        sp.drawArrow(x_temp, x_temp, y_temp, y_temp+self.troopDeployments[2][p+1], headlength=0.05, direction='U', lineColor='r')
                        
                    if (self.troopDeployments[1][p+1] > thresh) & (self.troopDeployments[2][p+1] > thresh):
                        sp.drawArrow(x_temp, x_temp+self.troopDeployments[1][p+1], y_temp, y_temp, headlength=0.05, direction='R', lineColor='r')
                        sp.drawArrow(x_temp+self.troopDeployments[1][p+1], x_temp+self.troopDeployments[1][p+1],
                                     y_temp, y_temp+self.troopDeployments[2][p+1], headlength=0.05, direction='U', lineColor='r')
                elif p ==4:
                    xfinal, yfinal, numsteps = sp.getFinalCoord(0, self.dx, self.dy, 0, x_temp, y_temp)
                    self.getWinner(xfinal, yfinal, numsteps)

            # battle proceeds until someone is annihilated
            sp.drawFinalVector(0, self.dx, self.dy, 0, x_temp, y_temp, stepsize=.1, colorVar ='b')

            # record strategies and outcome in csv
            self.csvwriter.writerow([self.playerNames[1], self.playerNames[2], self.troopDeployments[1][0], self.troopDeployments[1][1],
                                self.troopDeployments[1][2], self.troopDeployments[1][3], self.troopDeployments[1][4],
                                self.investment[1], self.troopDeployments[2][0], self.troopDeployments[1][1],
                                self.troopDeployments[2][2], self.troopDeployments[2][3], self.troopDeployments[2][4],
                    self.investment[2], self.battleWinner, self.battleLoser, self.remTroops, self.battleLength, self.gameTime])
 
            #save file and convert to gif
            sp.pngSave(outputName)
            ptg.pngToGif(outputName)

            # display photo to users
            simPhoto = PhotoImage(file=outputName+'.gif')
            self.photoLabel = Label(self.myContainer1, image=simPhoto)
            self.photoLabel.image = simPhoto
            self.photoLabel.grid(row=2, column=1, rowspan=20,columnspan=3, sticky=W)

            # ask players whether to quit or replay
            self.popupEnd()
            
        else:
            pass

    def getWinner(self, xfinal, yfinal, numsteps): # figure out which player had troops left and which one didn't
        if xfinal > yfinal:
            self.battleWinner = 1
            self.battleLoser = 2
            self.remTroops = xfinal*10000

        elif yfinal > xfinal:
            self.battleWinner = 2
            self.battleLoser = 1
            self.remTroops = yfinal*10000
        self.battleLength = numsteps

    def popupEnd(self): # announce who won, how long the battle took, and how many troops the winner had left; give option to quit or replay
        self.top = Toplevel()
        self.top.title("End of Round")
        self.top.geometry('300x170+830+400')

        msg = Label(self.top, text="%s beat %s\nin %d periods\nwith %d remaining troops." % (self.playerNames[self.battleWinner], self.playerNames[self.battleLoser], self.battleLength, self.remTroops)) 
        msg.grid(row=1, column=0, columnspan=4, rowspan=3)

        replayButton = Button(self.top, text="Replay", command=lambda: self.replay()) 
        replayButton.grid(row=4, column=1)

        quitButton = Button(self.top, text="Quit", command=lambda: root.destroy())
        quitButton.grid(row=4, column=2)

    def replay(self): # go back to point at which players enter their strategies
        self.top.destroy()
        self.currentPlayer = 1
        self.makeText('getStrategy')

def verifyQuit(): # when red "x" is clicked, verif that player wants to exit
    if tkMessageBox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy()
         

# initialize the game
root = Tk()
root.geometry('1100x700+150+40')    # size and position of the game window; width, height, w.offset, h.offset
root.protocol("WM_DELETE_WINDOW", verifyQuit) # make sure user wants to quit when they click "x" 
mygame = LanchesterSquares(root)    # place elements in window
root.title('Lanchester Squares')    # window title
root.mainloop()                     # start the game

#Behind-the-scenes functionality
#TODO: instructions


