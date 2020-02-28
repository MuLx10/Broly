import re
import copy
import requests
import config
import Channel
import Report.ContributionReport
import Social.RedditScrapper, Social.Horoscope
import Productivity.Productivity


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
       
    def get_social(self, type, contents = None):
        if type == 'horo':
            return Social.Horoscope.main()
        return Social.RedditScrapper.main(type, channel = contents['channel'], limit = contents['limit'])
                     
    def get_pr_stats(self, org_name, projects):
        return Productivity.Productivity.main(org_name, projects)
    
    def workflow_init(self):
        pass
        
    def post_report(self, report):
        message = "## Weekly Report\n"
        for r in report:
            #message += "<img src='"+str(r[1])[2:-1]+"' width='40' height='40'>\n\n"
            message += ">![img]("+str(r[1])[2:-1]+"&s=100)\n"
            message += ">**"+str(r[0])+" **\n"
            message += ">Commits:"+str(r[2])+'\n'
            message += ">PR Open: "+str(r[3])+", PR Closed:"+str(r[4])+'\n'
            message += ">Lines Added: "+str(r[5])+", Lines Added:"+str(r[6])+'\n'
            message += '\n'
        print(message)
        #print(report)
        self.channel.add_post(self.report_channel_id, message, self.headers)
    
    def post_social(self, type, contents):
        (image_urls, image_titles, image_ids) = contents
        print(contents)
        for url, title, _ in zip(image_urls, image_titles, image_ids):
            message = ''
            if type == 'tod':
                message += '## Thoughts ?\n'
            elif type == 'meme':
                message += "## "
            message += title+'\n'
            if not (type == 'tod'):
                message += "![img]("+url+")\n"
            message += '\n'
            print(message)
            self.channel.add_post(self.social_channel_id, message, self.headers)
    
    def post_productivity(self, stats):
        message = "# PR Status\n"
       
        for project in list(stats.keys()):
            prs = stats[project]
            message += "## "+project+'\n'
            for pr_no in list(prs.keys()):
                message +=  "["+str(pr_no)+"] **"+prs[pr_no]['title']+"**\n"
                message += '**' + prs[pr_no]['state'] + '** Created at: '+ prs[pr_no]['created_at']+'\n' 
                message += "**Labels: **"
                message += ', '.join(['_'+lb+'_' for lb in prs[pr_no]['labels']])
                message += "\n**Reviewers: **"
                message += ', '.join(['_'+rr+'_' for rr in prs[pr_no]['requested_reviewers']])
                message += '\n\n'
            print(message)
            self.channel.add_post(self.report_channel_id, message, self.headers)
            message = ""
    def post_workflow(self):
        pass

if __name__ == "__main__":
    bot = BrolyBot(team_id = config.TEAM_ID, token = config.BOT_API_KEY)
    
    report = bot.get_report('mattermost', ['mattermost-mobile'])
    bot.post_report(report)
    
    memes = bot.get_social('meme', {'channel':'ProgrammerHumor', 'limit':10})
    bot.post_social('meme', memes )
    
    tod = bot.get_social('tod', {'channel':'Showerthoughts', 'limit':1})
    bot.post_social('tod', tod )
    
    horo = bot.get_social('horo', {})
    bot.post_social('horo', horo )
    
    pr_stats = bot.get_pr_stats('mattermost', ['mattermost-mobile'])
    bot.post_productivity(pr_stats)