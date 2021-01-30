import praw
import csv
import re
import json   
import requests

reddit = praw.Reddit()

class StockPost(object):
    def __init__(self, postID, postURL, ups, downs, numComments, stock):
        self.postID = postID
        self.url = postURL
        self.stock = stock
        self.ups = ups
        self.downs = downs
        self.numComments = numComments
    
    def jsonEnc(self):
      return {'stock': self.stock, 'postID': self.postID, 'postURL': self.url, 'ups': self.ups, 'downs': self.downs, 'numComments': self.numComments}

def jsonDefEncoder(obj):
    if hasattr(obj, 'jsonEnc'):
        return obj.jsonEnc()
    else: #some default behavior
        return obj.__dict__

class SubredditScraper:

    def __init__(self, sub, sort='new', lim=900):
        self.sub = sub
        self.sort = sort
        self.lim = lim

        print(
            f'SubredditScraper instance created with values '
            f'sub = {sub}, sort = {sort}, lim = {lim}')

    def set_sort(self):
        if self.sort == 'new':
            return self.sort, reddit.subreddit(self.sub).new(limit=self.lim)
        elif self.sort == 'top':
            return self.sort, reddit.subreddit(self.sub).top(limit=self.lim)
        elif self.sort == 'hot':
            return self.sort, reddit.subreddit(self.sub).hot(limit=self.lim)
        else:
            self.sort = 'hot'
            print('Sort method was not recognized, defaulting to hot.')
            return self.sort, reddit.subreddit(self.sub).hot(limit=self.lim)

    def get_posts(self):

        stockTickers = {}
        with open('tickers.csv', mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                stockTickers[row[0]] = {}
        """Get unique posts from a specified subreddit."""

        # Attempt to specify a sorting method.
        sort, subreddit = self.set_sort()

        print(f'Collecting information from r/{self.sub}.')
        mentionedStocks = []
        i = 0
        for post in subreddit:
            i = i + 1
            print(i)
            if post.link_flair_text != 'Meme':
                for stock in stockTickers.keys():
                    if(re.search(r'\s+\$?' + stock + r'\$?\s+', post.selftext) or re.search(r'\s+\$?' + stock + r'\$?\s+',  post.title)):
                        stockTickers[stock][post.id] = StockPost(post.id, post.permalink, post.ups, post.downs, post.num_comments, stock)
        for stock in stockTickers:
            if (len(stockTickers[stock]) > 0):
                for post in stockTickers[stock]:
                    mentionedStocks.append(stockTickers[stock][post]) 
        json_object = json.dumps(mentionedStocks, default=jsonDefEncoder, indent = 4)   
        print(json_object)  


        headers = {'Content-type':'application/json', 'Accept':'application/json', 'Flamingo-Signature': "golaaaaa" }
        r = requests.post("https://localhost:44360/api/RedditPostsAdmin", data=json_object,  verify=False, headers=headers)
        print(r.status_code)
        



if __name__ == '__main__':
    SubredditScraper('wallstreetbets', lim=200, sort='hot').get_posts()