import os, sys

GH_API_KEY = os.getenv('GH_API_KEY', '')
REDDIT_API_CLIENT_ID = os.getenv('REDDIT_API_CLIENT_ID', '')
REDDIT_API_CLIENT_SECRET = os.getenv('REDDIT_API_CLIENT_SECRET', '')
REDDIT_API_USER_AGENT = "Meme collector"

BOT_API_KEY = os.getenv('BOT_API_KEY', '')
ADMIN_API_KEY = os.getenv('ADMIN_API_KEY', '')

TEAM_ID = "satzcatq1prftgtfz6c9m5x9my"
MATTERMOST_URL = "https://brolee.herokuapp.com"
ORG_NAME = 'mattermost'
PROJECTS = ['mattermost-mobile']



if __name__ == "__main__":
    get_teams = 'curl -i -H "Authorization: Bearer {token:s}" {MATTERMOST_URL:s}/api/v4/teams'.format(token = ADMIN_API_KEY, MATTERMOST_URL = MATTERMOST_URL)
    print(get_teams)
    os.system(str(get_teams))