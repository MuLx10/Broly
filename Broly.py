import config
import copy
import requests
import Channel
import Report.ContributionReport

class BrolyBot(object):
    """docstring for BrolyBot"""
    def __init__(self, team_id, token = config.BOT_API_KEY):
        super(BrolyBot, self).__init__() 
        self.team_id = team_id
        self.headers = {"Authorization": "Bearer {token:s}".format(token=token)} 
        
        
        self.channel = Channel.Channel(self.team_id)
        channels = self.channel.get_list()
        for c in channels:
            if c[1] == "town-square":
                self.report_channel_id = c[0]
            if c[1] == "off-topic":
                self.social_channel_id = c[0]
        
        #if self.report_channel_id is None:
        #    self.report_channel_id = self.channel.create(name="broly_reports", display_name = "Broly Reports", header = "**Broly Report**")
        #if self.social_channel_id is None:
        #    self.social_channel_id = self.channel.create(name="soci-tea", display_name = "Soci Tea", header = "**Soci Tea**")
    
    def get_report(self, org_name, projects):
        return Report.ContributionReport.main(org_name, projects)   
       
    def get_social(self):
        pass
                     
    def productivity_init(self):
        pass
    
    def workflow_init(self):
        pass
        
    def post_report(self, report):
        contributors = list(report.keys())
        attrb = ['avatar_url', 'no_of_commits','pr_open','pr_closed', 'lines_added', 'lines_removed']
        
        final_report = []
        for contributor in contributors:
            temp = [contributor]
            for a in attrb:
                temp.append(report[contributor][a])
            final_report.append(temp)
        
        final_report = sorted(final_report, key = lambda x: sum(x[2:5]), reverse = True)[:5]
        message = "## Weekly Report\n"
        
        for r in final_report:
            message += ">![img]("+str(r[1])[2:-1]+'&s=40)\n'
            message += ">**"+str(r[0])+"**\n"
            message += ">Commits:"+str(r[2])+'\n'
            message += ">PR Open: "+str(r[3])+", PR Closed:"+str(r[4])+'\n'
            message += '\n\n'
            
            
        print(message)
        #print(final_report)
        self.channel.add_post(self.report_channel_id, message, self.headers)
    
    def post_social(self):
        message = "**![dffd](https://avatars0.githubusercontent.com/u/23444642?s=40&v=4)**"
        self.channel.add_post(self.social_channel_id, message, self.headers)
       
    def post_workflow(self):
        pass
    
    def post_productivity(self):
        pass
    

if __name__ == "__main__":
    bot = BrolyBot(team_id = "satzcatq1prftgtfz6c9m5x9my", token = config.BOT_API_KEY)
    report = bot.get_report('mattermost', ['mattermost-mobile'])
    bot.post_report(report)
    bot.post_social()