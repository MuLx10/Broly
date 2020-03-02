# Broly

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


### Enable Access Token

### Create a bot


### Editing [config](config.py) file

```python
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
ORG_NAME = '' # Organization name on Github eg. 'mattermost'
PROJECTS = [] # list conatining projects eg. ['mattermost-mobile']
```
**Github API**
Resource can be found [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

**Reddit API**
Go to [app preferences](https://www.reddit.com/prefs/apps) and click on create app or create another app which will take you to this screen. For the redirect URL, put in http://localhost:8080

![](https://miro.medium.com/max/1866/1*3f6GfvGuHJIcqum74k3xBw.png)
![](https://miro.medium.com/max/1884/1*C-xVOOFOqV877jdZeCZ4sw.png)



### Get Teams

```bash
$ python config.py
```
