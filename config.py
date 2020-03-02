import os, sys

# Github API
GH_API_KEY = os.getenv('GH_API_KEY', '')

 # Reddit API
REDDIT_API_CLIENT_ID = os.getenv('REDDIT_API_CLIENT_ID', '') 
REDDIT_API_CLIENT_SECRET = os.getenv('REDDIT_API_CLIENT_SECRET', '')
REDDIT_API_USER_AGENT = "Meme collector"

BOT_API_KEY = os.getenv('BOT_API_KEY', '') # Mattermost Broly bot access token
ADMIN_API_KEY = os.getenv('ADMIN_API_KEY', '') # Mattermost Admin access token needed to get team ids (described below)

TEAM_ID = ""
MATTERMOST_URL = "https://mm-broly.herokuapp.com" # Mattermost url
ORG_NAME = 'mattermost' # Organization name on Github eg. 'mattermost'
PROJECTS = ['mattermost-mobile'] # list conatining projects eg. ['mattermost-mobile']



if __name__ == "__main__":
    get_teams = 'curl -i -H "Authorization: Bearer {token:s}" {MATTERMOST_URL:s}/api/v4/teams'.format(token = ADMIN_API_KEY, MATTERMOST_URL = MATTERMOST_URL)
    print(get_teams)
    os.system(str(get_teams))