import praw
import config
import random

class RedditScrapper(object):
    """docstring for RedditScrapper"""
    def __init__(self):
        super(RedditScrapper, self).__init__() 
        self.reddit = praw.Reddit(client_id = config.REDDIT_API_CLIENT_ID, 
                         client_secret = config.REDDIT_API_CLIENT_SECRET, 
                         user_agent = config.REDDIT_API_USER_AGENT)
                     
                     
    def get_scrape(self, channel, limit):
        subreddit = self.reddit.subreddit(channel) 
        posts = subreddit.hot(limit=limit)

        image_urls, image_titles, image_ids = [], [], []

        for post in posts:
          image_urls.append(post.url.encode('utf-8').decode("utf-8").encode("ascii", "ignore"))
          image_titles.append(post.title.encode('utf-8').decode("utf-8").encode("ascii", "ignore"))
          image_ids.append(post.id)
  
        return (image_urls, image_titles, image_ids)
    
    def get_thoughts(self, channel = 'Showerthoughts', limit = 1):
        return self.get_scrape(channel, limit)
    
    def get_memes(self, channel = 'ProgrammerHumor', limit = 10):
        return self.get_scrape(channel, limit)
      
      
m = RedditScrapper()
        
def main(type, channel, limit = 10):
    if type == 'tod':
        tod = m.get_thoughts(channel = channel, limit = limit+10)
        idx = 3+int(random.random()*7)
        #print(tod[0][idx], tod[1][idx], tod[2][idx])
        return [tod[0][idx]], [tod[1][idx]], [tod[2][idx]]
    if type == 'meme':
        return m.get_memes(channel = channel, limit = limit)
    
    
if __name__ == "__main__":
    main('Showerthoughts', 10)