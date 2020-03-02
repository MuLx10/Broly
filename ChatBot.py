from mmpy_bot.bot import respond_to
from mmpy_bot.bot import Bot
from Broly import BrolyBot
import config


bot = BrolyBot(team_id = config.TEAM_ID, token = config.BOT_API_KEY, post = False)
org_name = config.ORG_NAME
projects = config.PROJECTS

@respond_to('(.*)')
def give_me(message, request):
    print(request)
    if "report" in request.lower():
        report = bot.get_report(org_name, projects)
        reply = bot.post_report(report)
        
    if "meme" in request.lower():
        memes = bot.get_social('meme', {'channel':'ProgrammerHumor', 'limit':10})
        reply = bot.post_social('meme', memes )
    
    if "tod"in request.lower():
        tod = bot.get_social('tod', {'channel':'Showerthoughts', 'limit':1})
        reply = bot.post_social('tod', tod )
        
    if "horo" in request.lower():
        horo = bot.get_social('horo', {})
        reply = bot.post_social('horo', horo )
        
    if "pr" in request.lower():
        pr_stats = bot.get_pr_stats(org_name, projects)
        reply = bot.post_productivity(pr_stats)
    
    message.reply(reply)

if __name__ == "__main__":
    print("Bot is listening....\n")
    Bot().run()