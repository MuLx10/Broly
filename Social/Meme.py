import praw
import config

class Meme(object):
    """docstring for Meme"""
    def __init__(self):
        super(Meme, self).__init__() 
        self.reddit = praw.Reddit(client_id = config.REDDIT_API_CLIENT_ID, 
                         client_secret = config.REDDIT_API_CLIENT_SECRET, 
                         user_agent = config.REDDIT_API_USER_AGENT)
                     
                     
    def get_memes(self, channel, limit):
        subreddit = self.reddit.subreddit(channel) 
        posts = subreddit.hot(limit=limit)

        image_urls, image_titles, image_ids = [], [], []
        for post in posts:
          image_urls.append(post.url.encode('utf-8'))
          image_titles.append(post.title.encode('utf-8'))
          image_ids.append(post.id)
  
        return (image_urls, image_titles, image_ids)
        
def main(channel = 'ProgrammerHumor', limit = 10):
    m = Meme()
    return m.get_memes(channel = channel, limit = limit)
if __name__ == "__main__":
    main()