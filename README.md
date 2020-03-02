# Broly

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Setup
### Enable Access Token

Go to System Console -> Integration Management
Follow steps 1->2->3
![](https://github.com/MuLx10/Broly/raw/master/images/access_token.png)

### Create a bot

Enable Bot Accounts
![](https://github.com/MuLx10/Broly/raw/master/images/bot_acc.png)

Create Bots
![](https://github.com/MuLx10/Broly/raw/master/images/new_bot1.png)
![](https://github.com/MuLx10/Broly/raw/master/images/new_bot2.png)

Note the Bot access token, It is needed as API Key for commandline
![](https://github.com/MuLx10/Broly/raw/master/images/bot_token.png)

### Editing [config](config.py) file

```python
# Github API
GH_API_KEY = os.getenv('GH_API_KEY', 'Fill here or add to the environment variable')

# Reddit API
REDDIT_API_CLIENT_ID = os.getenv('REDDIT_API_CLIENT_ID', 'Fill here or add to the environment variable') 
REDDIT_API_CLIENT_SECRET = os.getenv('REDDIT_API_CLIENT_SECRET', 'Fill here or add to the environment variable')
REDDIT_API_USER_AGENT = "Meme collector"

BOT_API_KEY = os.getenv('BOT_API_KEY', 'Fill here or add to the environment variable') # Mattermost Broly bot access token
ADMIN_API_KEY = os.getenv('ADMIN_API_KEY', 'Fill here or add to the environment variable') # Mattermost Admin access token needed to get team ids (described below)
MATTERMOST_URL = "https://mm-broly.herokuapp.com" # Mattermost url
```
**Github API**
Resource can be found [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

**Reddit API**
Go to [app preferences](https://www.reddit.com/prefs/apps) and click on create app or create another app which will take you to this screen. For the redirect URL, put in http://localhost:8080

![](https://miro.medium.com/max/1866/1*3f6GfvGuHJIcqum74k3xBw.png)
![](https://miro.medium.com/max/1884/1*C-xVOOFOqV877jdZeCZ4sw.png)

### Get Teams
Account Settings -> Security -> Personal Access Tokens

```bash
$ python config.py
[{"id":"xh956esr83bhpkom35zekfzxdy","create_at":1583095734153,"update_at":1583095734153,"delete_at":0,"display_name":"BotFest","name":"botfest","description":"","email":"test@test.com","type":"O","company_name":"","allowed_domains":"","invite_id":"h6cfgdpjh3neumfgeba9oy55qe","allow_open_invite":false,"scheme_id":null,"group_constrained":null}]
```

Choose the team id and add it in config.py

```python 
TEAM_ID = "xh956esr83bhpkom35zekfzxdy"
ORG_NAME = 'mattermost' # Organization name on Github eg. 'mattermost'
PROJECTS = ['mattermost-mobile'] # list conatining projects eg. ['mattermost-mobile']
```

## Run

```bash
$ python app.py
```

### Usage

Broly has two parts.
- Cron Job : Scheduled jobs which are performed on a fixed time interval
  - Start with a intriguing thought of the day
  - Prepare and post Weekly report
  - Present a daily dose of memes
  - Gather status of PR on daily basis
  - Daily Horoscope
- Chatbot : The above things can also be request at will
  - Meme: Broly share a meme
  - Thought of the day: Give me a tod
  - Report: Show contribution report
  - PR status: pr status
  - Horoscope: horoscope
  
  
  ### Screenshots
  
  


