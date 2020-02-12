import config
import copy
import requests
import Channel
headers = {"Authorization": "Bearer {token:s}".format(token=config.BOT_API_KEY)} 

class BrolyBot(object):
    """docstring for BrolyBot"""
    def __init__(self, team_id, token = config.BOT_API_KEY):
        super(BrolyBot, self).__init__() 
        self.team_id = team_id
        self.headers = {"Authorization": "Bearer {token:s}".format(token=token)} 
        self.channel_id = None
        self.report_init()
    
    def report_init(self):
        self.channel = Channel.Channel(self.team_id)
        channels = self.channel.get_list()
        for c in channels:
            if c[1] == "broly_reports":
                self.channel_id = c[0]
        
        if self.channel_id is None:
            self.channel_id = self.channel.create(name="broly_reports", display_name = "Broly Reports", header = "**Broly Report**")
            
    def social_init(self):
        pass
    
    def workflow_init(self):
        pass
        
    def post_report(self):
        message = "**![dffd](https://avatars0.githubusercontent.com/u/23444642?s=460&v=4)**"
        self.channel.add_post(self.channel_id, message, headers)
    
    def post_social(self):
        pass
       
    def post_workflow(self):
        pass
    

if __name__ == "__main__":
    bot = BrolyBot(team_id = "satzcatq1prftgtfz6c9m5x9my", token = config.BOT_API_KEY)
    bot.post_report()