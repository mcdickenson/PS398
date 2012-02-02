# learning to understand inheritance
# we'll use football players and baseball players

# What do football players have?
# name, height, weight, number

# What do baseball players have?
# name, height, weight, number

# so we can abstract that into class Athlete():

# What is unique about each?
# football players have yards (some, at least); special teams/offense/defense
# baseball players have batting avg; AL/NL
# these are all data things we can model

class Athlete(object):

    def __init__(self, name, height, weight, number):

        self.name = name
        self.height = height
        self.weight = weight
        self.number = number

    def endorse(self):
        return "I endorse things"

class BaseballPlayer(Athlete):

    def set_batting_average(self, average):
        self.batting_avg = average

    def get_batting_average(self): # note use of set, get
        return self.batting_average

    def set_AL(self, al):
        self.AL = False

    def endorse(self):
        return "I, " + str(self.name) + ", endorse Rawlings."

class FootballPlayer(Athlete):

    def set_special_teams(self, sp_teams):
        self.special_teams = sp_teams

    def get_special_teams(self):
        return self.special_teams

    def endorse(self):
        return "I, " + str(self.name) + ", endorse football things."

    
