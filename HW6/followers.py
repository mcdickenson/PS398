"""Homework 6: Twitter API
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW6/

### SETUP
#Register an app: https://dev.twitter.com/

#pip install tweepy
import tweepy

#First parameter is Consumer Key, second is Access Token 
auth = tweepy.OAuthHandler('dcR9xvSBhVuc3vJsqa8T4w', '')
auth.set_access_token('202203453-YQboa4abf85kYpUO4RxmBIQmB5dKsFjY2KSQYPjc', '')    
api = tweepy.API(auth)

# see rate limit
api.rate_limit_status()

# see most recent 20 tweets (refreshes every 60 seconds, calling more often is useless)
public_tweets = api.public_timeline()
for t in public_tweets:
    print"{0}: {1}".format(t.user.screen_name.encode('ascii', 'ignore'), t.text.encode('ascii', 'ignore'))

# Get some users

monkey = api.get_user('monkeycageblog')

# Who does MonkeyCageBlog follow?
monkey_friends = api.friend(id=monkey.screen_name)
for fr in monkey_friends:
    print "{0}".format(fr.screen_name.encode('ascii', 'ignore'))

# Who follows MonkeyCageBlog?
monkey_followers = api.followers(id=monkey.screen_name)
num_followers = 0 
follower_list = {}
for fl in monkey_followers:
    print "{0}".format(fl.screen_name.encode('ascii', 'ignore'))
    num_followers += 1
    follower_list.append() # add screen_name as key, number of followers as return
    # use followers_count
    # https://dev.twitter.com/discussions/605
    # https://github.com/sixohsix/twitter
    # https://dev.twitter.com/docs/things-every-developer-should-know
