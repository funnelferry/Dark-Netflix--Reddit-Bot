import praw
import config
import re

def bot_login():
    r = praw.Reddit(username = config.username,
	       password = config.password,
	       client_id = config.client_id,
	       client_secret = config.client_secret,
	       user_agent = "wenzwen responder 1.0")
    return r

# Following function, iterates over the comments of reddit.com/r/test
# and is a simple example of use of Regular Expressions, It identifies if the words 'why, what, how, which, where' 
# are there in a comment and replace all the instances with 'when'
# In case you don't know it is a running joke from the German Netflix Original 'Dark'
# This bot is aimed to work for reddit.com/r/DarkTV 

def run_bot(r):
	for comment in r.subreddit('test').comments(limit=25):
		findw = re.compile(r'why|what|how|which|where',re.I)
		if findw.search(comment.body):
			s = comment.body
			r = findw.sub('when', s)
			final = r.capitalize()
			print(final)
			
		
r = bot_login()
run_bot(r)	