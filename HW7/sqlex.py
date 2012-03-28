#pip install sqlalchemy, pip install pysqlite
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#Some info about sqlalchemy
print sqlalchemy.__version__

#Connect to the local database, can use :memory: to just try it out in memory
#Replace inclass.db with :memory: to avoid writing to disk
engine = sqlalchemy.create_engine('sqlite:////inclass.db', echo=True)

Base = declarative_base()

# Everything above HERE is boilerplate, pretty much needed for any Python script that interacts with SQL

#Define some schemas
class Player(Base):
  __tablename__ = 'players' # convention is always to take the object name & pluralize
  
  #Have an ID column because player attributes (name, etc) are not unique
  id = Column(Integer, primary_key=True) # this will always be a unique integer
  name = Column(String)
  number = Column(Integer)
  
  team_id = Column(Integer, ForeignKey("teams.id")) # references teams.id table
  
  def __init__(self, name, number, team=None):
    self.name = name
    self.number = number
    self.team = team
    
  def __repr__(self):
    return "<Player('%s', '%s')>" % (self.name, self.number)


class Team(Base):
  __tablename__ = "teams"
  
  id = Column(Integer, primary_key=True)
  name = Column(String)
  players = relationship("Player", backref="team") # unique to the ORM; note the reciprocity
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "<team('%s')>" % (self.name)

#First time create tables
Base.metadata.create_all(engine) 

#See structure of players table:
Player.__table__  

#Create a player
mason = Player("Mason Plumlee", 5)
str(mason.id) # this is just an object so far, not associated with the table

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()
# Sessions are tied to a bunch of wonderful things called transactions that you can look up on your own

session.add(mason) # this 'persists', ie stores, the object by adding to database
                   # but it's done in batches, so if you print right away it may not have happened yet
 
#Create some more players
session.add_all([
  Player("Miles Plumlee", 40),
  Player("Seth Curry", 30),
  Player("Austin Rivers", 0),
  Player("The other Plumlee", 100)
])

#Persist all of this information (to disk)
session.commit()
str(mason.id)

#Some querying
#What gets returned is an array/list of objects
#Notice that we are calling objects, not tables per se
#order the results
for player in session.query(Player).order_by(Player.number):
  print player.number, player.name
  
#limit the results with offset, might use this for pagination
#Notice the indexing of the result
for player in session.query(Player).order_by(Player.number)[1:3]:
  print player.number, player.name

#Some filters
#All of these are composable, meaning they can be used together
for player in session.query(Player).filter(Player.name == "Mason Plumlee").order_by(Player.number):
  print player.number, player.name

  # Notice that we are using Python logical statements 
for player in session.query(Player).filter(Player.name != "Mason Plumlee").order_by(Player.number):
  print player.number, player.name

  # Notice the use of or_
for player in session.query(Player).filter(or_(Player.name == "Mason Plumlee", Player.name == "Miles Plumlee")).order_by(Player.number):
  print player.number, player.name

  # sql supports a like operator, which is kind of neat
for player in session.query(Player).filter(Player.name.like("%Plumlee%")).order_by(Player.number):
  print player.number, player.name

  # Notice the use of and_
for player in session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number):
  print player.number, player.name

#Results are just lists  
results = session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number)
results.first()

#count is faster than loading all of the objects
#this is MUCH faster than loading all of the objects in Python and counting them
session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number).count()

#how to work with relations
duke = Team('Duke')

players = session.query(Player).all()
mason.team = duke
players[1].team = duke
mason.team.players

str(duke.id)

#Lets load the two things together
#This is an inner join
for player, team in session.query(Player, Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print player.number, player.name, team.name

#equivalently, query on players & join on team  
for player in session.query(Player).join(Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print player.number, player.name, player.team.name

#Now some deletion (see SQLAlchemy Cascades for some fun data sanitation)
players
session.query(Player).filter(Player.number == 30).count()
seth = session.query(Player).filter(Player.number == 30).first()
session.delete(seth)
session.query(Player).filter(Player.number == 30).count()
players

#Updating
other_plumlee = players[4]
other_plumlee.name = "Marshall Plumlee"
session.dirty # tells you what has changed since last commit
session.commit()
