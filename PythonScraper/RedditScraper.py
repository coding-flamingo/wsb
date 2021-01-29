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
        print(len(mentionedStocks))
        json_object = json.dumps(mentionedStocks, default=jsonDefEncoder, indent = 4)   
        print(json_object)  
        headers = {'Content-type':'application/json', 'Accept':'application/json', 'Igalito-Signature': "golaaaaa" }
        json_object = '[\n    {\n        "stock": "AAPL",\n        "postID": "l873f0",\n        "postURL": "/r/wallstreetbets/comments/l873f0/a_comprehensive_guide_to_some_moments_in_wsb/",\n        "ups": 57,\n        "downs": 0,\n        "numComments": 11\n    },\n    {\n        "stock": "ASAN",\n        "postID": "l86lem",\n        "postURL": "/r/wallstreetbets/comments/l86lem/my_ask_of_you_pay_it_forward_for_autism/",\n        "ups": 400,\n        "downs": 0,\n        "numComments": 74\n    },\n    {\n        "stock": "DD",\n        "postID": "l873f0",\n        "postURL": "/r/wallstreetbets/comments/l873f0/a_comprehensive_guide_to_some_moments_in_wsb/",\n        "ups": 57,\n        "downs": 0,\n        "numComments": 11\n    },\n    {\n        "stock": "GD",\n        "postID": "l873ev",\n        "postURL": "/r/wallstreetbets/comments/l873ev/we_do_not_just_hold_gme_we_buy_more_for_dfv/",\n        "ups": 88,\n        "downs": 0,\n        "numComments": 22\n    },\n    {\n        "stock": "GME",\n        "postID": "l873f0",\n        "postURL": "/r/wallstreetbets/comments/l873f0/a_comprehensive_guide_to_some_moments_in_wsb/",\n        "ups": 57,\n        "downs": 0,\n        "numComments": 11\n    },\n    {\n        "stock": "GME",\n        "postID": "l873ev",\n        "postURL": "/r/wallstreetbets/comments/l873ev/we_do_not_just_hold_gme_we_buy_more_for_dfv/",\n        "ups": 88,\n        "downs": 0,\n        "numComments": 22\n    },\n    {\n        "stock": "GME",\n        "postID": "l86ku5",\n        "postURL": "/r/wallstreetbets/comments/l86ku5/if_you_have_gme_options_that_are_deep_itm/",\n        "ups": 149,\n        "downs": 0,\n        "numComments": 53\n    },\n    {\n        "stock": "GME",\n        "postID": "l86i72",\n        "postURL": "/r/wallstreetbets/comments/l86i72/i_put_5k_in_gme_at_33_could_have_pulled_for_113k/",\n        "ups": 694,\n        "downs": 0,\n        "numComments": 77\n    },\n    {\n        "stock": "HEAR",\n        "postID": "l871dq",\n        "postURL": "/r/wallstreetbets/comments/l871dq/im_furious/",\n        "ups": 282,\n        "downs": 0,\n        "numComments": 45\n    },\n    {\n        "stock": "ONE",\n        "postID": "l873ev",\n        "postURL": "/r/wallstreetbets/comments/l873ev/we_do_not_just_hold_gme_we_buy_more_for_dfv/",\n        "ups": 88,\n        "downs": 0,\n        "numComments": 22\n    },\n    {\n        "stock": "OUT",\n        "postID": "l86tla",\n        "postURL": "/r/wallstreetbets/comments/l86tla/im_not_settling_for_a_home_run_we_want_a_grand/",\n        "ups": 443,\n        "downs": 0,\n        "numComments": 140\n    },\n    {\n        "stock": "PRPL",\n        "postID": "l873f0",\n        "postURL": "/r/wallstreetbets/comments/l873f0/a_comprehensive_guide_to_some_moments_in_wsb/",\n        "ups": 57,\n        "downs": 0,\n        "numComments": 11\n    },\n    {\n        "stock": "TSLA",\n        "postID": "l873f0",\n        "postURL": "/r/wallstreetbets/comments/l873f0/a_comprehensive_guide_to_some_moments_in_wsb/",\n        "ups": 57,\n        "downs": 0,\n        "numComments": 11\n    },\n    {\n        "stock": "TV",\n        "postID": "l878qm",\n        "postURL": "/r/wallstreetbets/comments/l878qm/history_in_the_making/",\n        "ups": 23,\n        "downs": 0,\n        "numComments": 4\n    }\n]'
        payload = json_object
        r = requests.post("https://localhost:44360/api/RedditPostsAdmin", data=payload,  verify=False, headers=headers)
        print(r.status_code)
        



if __name__ == '__main__':
    SubredditScraper('wallstreetbets', lim=5, sort='new').get_posts()