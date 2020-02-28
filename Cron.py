import config
from Broly import BrolyBot
from apscheduler.schedulers.blocking import BlockingScheduler

print("Starting schedulers")

org_name = 'mattermost'
projects = ['mattermost-mobile']

bot = BrolyBot(team_id = config.TEAM_ID, token = config.BOT_API_KEY)

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every minute.')
    
@sched.scheduled_job('cron', day_of_week='mon', hour=9)
def scheduled_job():
    report = bot.get_report(org_name, projects)
    bot.post_report(report)
    print('This job is run every day at 9am.')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=9)
def scheduled_job():
    tod = bot.get_social('tod', {'channel':'Showerthoughts', 'limit':1})
    bot.post_social('tod', tod )
    print('This job is run every day at 9am.')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10)
def scheduled_job():
    horo = bot.get_social('horo', {})
    bot.post_social('horo', horo )
    print('This job is run every day at 10am.')
    
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=13)
def scheduled_job():
    memes = bot.get_social('meme', {'channel':'ProgrammerHumor', 'limit':10})
    bot.post_social('meme', memes )
    print('This job is run every day at 1pm.(Lunch break)') 
    
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=17)
def scheduled_job():
    pr_stats = bot.get_pr_stats(org_name, projects)
    bot.post_productivity(pr_stats)
    print('This job is run every day at 5pm.') 

sched.start()
