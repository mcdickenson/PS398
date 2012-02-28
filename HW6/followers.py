"""Homework 6: Twitter API
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW6/

### SETUP
#Register an app: https://dev.twitter.com/

#easy_install tweepy
import tweepy, csv, time
from os.path import exists

class myAPI(object):

    def __init__(self, target_name):
        self.auth = tweepy.OAuthHandler('get your own stinking key', '')
        self.auth.set_access_token('get your own stinking key', '')       
        self.api = tweepy.API(self.auth)

        # Set target
        self.target_name = target_name
        self.target_user = self.api.get_user(target_name)
        self.target_num_followers = len(self.api.followers_ids(self.target_user.screen_name)) 
        self.target_num_friends = len(self.api.friends_ids(self.target_user.screen_name))  
        self.status_filename = str(self.target_name) + '_overall_status.txt'

        if exists(self.status_filename):              
            self.statusHandler()
        else:
            self.writeStatus('findfrnd')
            self.statusHandler()

    def __str__(self):
        return "%s follows %d users and is followed by %d friends." % (self.target_name, self.target_num_friends, self.target_num_followers)
        
    def writeStatus(self, new_status):
        writefile = open(self.status_filename, "wb")
        writefile.write(str(new_status))
        writefile.close()
    
    def statusHandler(self):
        '''Load status of program at last run.'''
        status_file = open(self.status_filename)
        status = status_file.read()
        status = status[0:8] # defensive programming
        status_file.close()  

        if status =='findflwr': 
            # create file for most followed user that follows the target
            Headers = ["Username", "Checked", "Followers List", "Followers Count"]
            nameOutput = str(self.target_name)+"_followers_s1.csv"
            self.outputFile = open(nameOutput,"wb")
            csvwriter = csv.writer(self.outputFile)
            csvwriter.writerow(Headers)
            self.find_target_followers(csvwriter)

        elif status == 'findfrnd':
            # create file of users that target follows
            Headers = ["Username", "Checked", "Activity Level"]
            nameOutput = str(self.target_name)+"_most_active_s-1.csv"
            self.outputFile = open(nameOutput,"wb")
            csvwriter = csv.writer(self.outputFile)
            csvwriter.writerow(Headers)
            self.find_friends(csvwriter)

        elif status == 'FrndDetl':
            # create file for detils of target's friends 
            Headers = ["Username", "Checked", "Status count", "Start date", "Favorites", "Location", "Website"]
            nameOutput = str(self.target_name)+"_active_details_s-1.csv"
            outputFile = open(nameOutput,"a")
            csvwriter = csv.writer(outputFile)
            csvwriter.writerow(Headers)
            print "File created."
            nameInput = str(self.target_name)+"_most_active_s-1.csv"
            inputFile = open(nameInput, "rU")
            csvreader = csv.reader(inputFile)
            self.friend_details(csvwriter, csvreader)
        
        elif status == 'most_fs1':
            Headers = ["Username", "Checked", "Followers Count"]
            nameOutput = str(self.target_name)+"_most_followed_s1.csv"
            self.outputFile = open(nameOutput,"ab")
            csvwriter = csv.writer(self.outputFile)
            csvwriter.writerow(Headers)
            nameInput = str(self.target_name)+"_followers_s1.csv"
            self.inputFile = open(nameInput,"rU")
            csvreader = csv.reader(self.inputFile)
            self.most_followed_s1(csvwriter,csvreader)

        elif status == 'mstfs15k':
            Headers = ["Username", "Checked", "Status count", "Start date", "Followers count", "Favorites", "Website"]
            nameOutput = str(self.target_name)+"_5kfollows_s1.csv"
            self.outputFile = open(nameOutput,"ab")
            csvwriter = csv.writer(self.outputFile)
            csvwriter.writerow(Headers)
            nameInput = str(self.target_name)+"_most_followed_s1.csv"
            self.inputFile = open(nameInput,"rU")
            csvreader = csv.reader(self.inputFile)
            self.most_followed_s1_for_5000(csvwriter,csvreader)

    ### SEARCHING
    def get_rate_limit(self):
        '''See my API rate limit.'''
        limit = self.api.rate_limit_status()
        return limit

    def get_remaining_requests(self):
        '''How many API requests do I have this hour? When will it refresh?'''
        pass

    def most_recent_public_20():
        '''see most recent 20 tweets (refreshes every 60 seconds, calling more often is useless)'''
        public_tweets = self.api.public_timeline()
        for t in public_tweets:
            print"{0}: {1}".format(t.user.screen_name.encode('ascii', 'ignore'), t.text.encode('ascii', 'ignore'))

    def find_friends(self, csvwriter):
        '''Who does the target follow?'''
        self.target_num_friends = 0 
        for page in tweepy.Cursor(self.api.friends, id=self.target_user.screen_name).pages():
            for friend in page:
                name = str("{0}".format(friend.screen_name.encode('ascii', 'ignore')))
                print name
                csvwriter.writerow([name,0,0])
                self.target_num_friends += 1
        self.outputFile.close()
        print "%s follows %d users." % (self.target_name, self.target_num_friends)
        #self.writeStatus('findflwr')
        #self.statusHandler()

    def friend_details(self, csvwriter, csvreader):
        friend_file = csvreader
        numExcept = 0 
        for row in friend_file:
            if row[1] == '0':
                username = str(row[0])
                print username
                try:
                    temp_user = self.api.get_user(username)
                    user_state = temp_user.__getstate__()
                    print user_state
                    status_count = user_state['statuses_count']
                    start_date = user_state['created_at']
                    favorites = user_state['favourites_count']
                    location =str( user_state['location'])
                    website = user_state['url']
                    csvwriter.writerow([username, 1, status_count, start_date, favorites, location, website])
                    print "I worked."
                except tweepy.TweepError, UnicodeEncodeError:
                    csvwriter.writerow([username, 1, 'NA', 'NA', 'NA', 'NA', 'NA'])
                    print "Caught exception."
                    numExcept += 1
                    if numExcept >=5:
                        break
                    time.sleep(1)
            else: print "Line skipped."

        
    def find_target_followers(self, csvwriter):
        '''Who follows our target?'''
        for page in tweepy.Cursor(self.api.followers, id=self.target_user.screen_name).pages():
            for follower in page:
                name = str("{0}".format(follower.screen_name.encode('ascii', 'ignore')))
                csvwriter.writerow([name,0,0])
        print "%s has %d followers." % (self.target_name, self.target_num_followers)
        self.outputFile.close()
        self.writeStatus('most_fs1')
        self.statusHandler()


    def most_followed_s1(self, csvwriter, csvreader):
        follower_file = csvreader
        numExcept = 0 
        for row in follower_file:
            if row[1] == '0':
                name_to_check = str(row[0])
                try: 
                    followers = self.api.followers_ids(name_to_check)
                    follower_count = len(followers)
                    csvwriter.writerow([name_to_check, 1, follower_count])
                    numExcept = 0 
                    print "I worked."
                except tweepy.TweepError:
                    csvwriter.writerow([name_to_check, 1, 'NA'])
                    print "Caught exception."
                    numExcept += 1
                    if numExcept >=5:
                        break
                    time.sleep(1)
            else: print "Line skipped."
        self.outputFile.close()
        self.writeStatus('FrndDetl')
        self.statusHandler()

    def most_followed_s1_for_5000(self, csvwriter, csvreader):
        follow_file = csvreader
        numExcept = 0 
        for row in follow_file:
            print row[2]
            if row[2] == '5000':
                username = str(row[0])
                print username
                try:
                    temp_user = self.api.get_user(username)
                    user_state = temp_user.__getstate__()
                    print user_state
                    status_count = user_state['statuses_count']
                    start_date = user_state['created_at']
                    follower_count = user_state['followers_count']
                    favorites = user_state['favourites_count']
                    website = user_state['url']
                    csvwriter.writerow([username, 1, status_count, start_date, follower_count, favorites, website])
                    print "I worked."
                except tweepy.TweepError, UnicodeEncodeError:
                    csvwriter.writerow([username, 1, 'NA', 'NA', 'NA', 'NA', 'NA'])
                    print "Caught exception."
                    numExcept += 1
                    if numExcept >=5:
                        break
                    time.sleep(1)
            else: print "Line skipped."

    def most_followed_s2(self, csvwriter, csvreader):
        pass


# RUN
monkeyAPI = myAPI('monkeycageblog')
# Monkey Cage's most-followed follwer is Nate Silver (fivethirtyeight)
 
# Most active user (as measured by number of tweets): Matt Yglesias
# mattyAPI = myAPI('mattyglesias')
# Dave Weigel (daveweigel) is Matt Yglesias's most active friend 
