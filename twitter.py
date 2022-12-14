'''
Random Twitter

The aim of the project is to go and check the twitter follower
and tweet on of the random follower

'''

import twitter
import random

api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')

followers=api.Getfollowers()
randomindex=random.randint(0,len(followers)-1)
randomFollowers=followers[randomindex]

print(randomFollowers.screen_name)

tweet=f"@{randomFollowers.screen_name} you are the random follower of the day "
api.PostUpdate(tweet)
print(tweet)
print("Thanks for tweeting")

