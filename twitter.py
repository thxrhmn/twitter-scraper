import pandas as pd
from tqdm import tqdm
import snscrape.modules.twitter as sntwitter
import argparse
import os

print('''
  _______       _ _   _                 
 |__   __|     (_) | | |                
    | |_      ___| |_| |_ ___ _ __      
    | \ \ /\ / / | __| __/ _ \ '__|     
    | |\ V  V /| | |_| ||  __/ |        
   _|_|_\_/\_/ |_|\__|\__\___|_|        
  / ____|                               
 | (___   ___ _ __ __ _ _ __   ___ _ __ 
  \___ \ / __| '__/ _` | '_ \ / _ \ '__|
  ____) | (__| | | (_| | |_) |  __/ |   
 |_____/ \___|_|  \__,_| .__/ \___|_|   
                       | |              
   github.com/thxrhmn  |_|        
''')

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help='Username yang akan di scrape', type=str)
parser.add_argument('-t', '--total', help='Total tweet yang akan di scrape', type=str)
args = parser.parse_args()

scraper = sntwitter.TwitterUserScraper(args.username)

tweets = []
n_tweet = int(args.total)
file_name = args.username + ".csv"

for i, tweet in tqdm(enumerate(scraper.get_items()), total=n_tweet):
    data = [
        tweet.date,
        tweet.url,
        tweet.rawContent,
        tweet.replyCount,
        tweet.retweetCount,
        tweet.likeCount,
        tweet.viewCount,
    ]
    tweets.append(data)
    if i > n_tweet:
        break

tweet_df = pd.DataFrame(tweets, columns=["date","url","content","reply","retweet","like","view"])
tweet_df.to_csv(file_name, index=False)