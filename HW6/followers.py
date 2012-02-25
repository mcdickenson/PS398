"""Homework 6: Twitter API
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW6/

### SETUP
#Register an app: https://dev.twitter.com/

#easy_install tweepy
import tweepy
import csv
from os.path import exists

class myAPI(object):

    def __init__(self, target_name):
        #First parameter is Consumer Key, second is Access Token 
        self.auth = tweepy.OAuthHandler('dcR9xvSBhVuc3vJsqa8T4w', '')
        self.auth.set_access_token('202203453-YQboa4abf85kYpUO4RxmBIQmB5dKsFjY2KSQYPjc', '')    
        self.api = tweepy.API(self.auth)

        # Set target
        self.target_name = target_name
        self.target_user = self.api.get_user(target_name)
        self.target_num_followers = 0 
        self.target_num_friends = 0

# Also: created a supplementary file for preserving status between runs
# overall_status.txt    will save which of the four parts of the assignment I'm on
#                       initially contains "firstrun" 

        check_filename = str(self.target_name) + '_overall_status.txt'
        if exists(check_filename):  
            status_file = open(check_filename)
            status = status_file.read()
            status = status[0:8] # defensive programming
            status_file.close()
            self.status_handler(status)
        else:
            writefile = open(check_filename, "wb")
            writefile.write('firstrun')
            writefile.close()
            status = 'firstrun' # 'firstrun'
            self.status_handler(status)

    def __str__(self):
        return "%s follows %d users and is followed by %d friends." % (self.target_name, self.target_num_friends, self.target_num_followers)
    
    def status_handler(self, status):
        '''Load status of program at last run.'''        

        if status =='firstrun': 
            # create file for most followed user that follows the target
            Headers = ["Username", "Checked", "Followers List", "Followers Count"]
            nameOutput = str(self.target_name)+"_most_followed_s1.csv"
            outputFile = open(nameOutput,"wb")
            csvwriter = csv.writer(outputFile)
            csvwriter.writerow(Headers)
            #self.find_target_followers(csvwriter)
            self.find_friends(csvwriter)
            #most_followed_s1(outputFile)

        elif status == 'findfrnd':
            # create file of users that target follows
            Headers = ["Username", "Checked", "Activity Level"]
            nameOutput = str(target_name)+"_most_active_s-1.csv"
            outputFile = open(nameOutput,"wb")
            csvwriter = csv.writer(outputFile)
            csvwriter.writerow(Headers)
            self.find_friends(csvwriter)  
            outputFile.close()
        
        elif status == 'most_fs1':
            pass
        #    no need to create file, just load it
    
# most_followed_s1.csv  
# most_followed_s2.csv  
# most_active_s2.csv
# most_active_s-1.csv

### STORING
# Because of the rate limit (see above), we need to save search status as we go

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
        target_friends = self.api.friends(id=self.target_user.screen_name)
        self.target_num_friends = 0
        for fr in target_friends:
            name = str("{0}".format(fr.screen_name.encode('ascii', 'ignore')))
            print name
            csvwriter.writerow([name,0,0])
            self.target_num_friends += 1
        print "%s follows %d users." % (self.target_name, self.target_num_friends)

    def find_target_followers(self, csvwriter):
        '''Who follows our target?'''
        target_followers = self.api.followers(id=self.target_user.screen_name)
        follower_list = {}
        self.target_num_followers = 0 
        for fl in target_followers:
            name = str("{0}".format(fl.screen_name.encode('ascii', 'ignore')))
            print name
            csvwriter.writerow([name,0,0])
            target_num_followers += 1
            #follower_list.append() # add screen_name as key, number of followers as return
        # use followers_count
        print "%s has %d followers." % (self.target_name, self.target_num_followers)
        # https://dev.twitter.com/discussions/605
        # https://github.com/sixohsix/twitter
        # https://dev.twitter.com/docs/things-every-developer-should-know


    def most_followed_s1(outputFile):
        pass
    
    #def where_to_start(outputFile):
    #    for row in outputFile

# RUN
monkeyAPI = myAPI('monkeycageblog')
