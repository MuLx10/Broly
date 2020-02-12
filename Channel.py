import config
import copy
import requests

headers = {"Authorization": "Bearer {token:s}".format(token=config.ADMIN_API_KEY)} 

class Channel(object):
    """docstring for Channel"""
    def __init__(self, team_id):
        super(Channel, self).__init__() 
        self.team_id = team_id
    
    def create(self, name, display_name="", purpose="", header="", type='O'):
        '''
        string Required
        The team ID of the team to create the channel on

         name	
        string Required
        The unique handle for the channel, will be present in the channel URL

         display_name	
        string Required
        The non-unique UI name for the channel

         purpose	
        string
        A short description of the purpose of the channel

         header	
        string
        Markdown-formatted text to display in the header of the channel

         type	
        string Required
        'O' for a public channel, 'P' for a private channel
        '''
        display_name =  name if (display_name == "") else display_name
        header =  name if (header == "") else header
        
        body = {}
        body["team_id"] = self.team_id
        body["name"] = name
        body["display_name"] = display_name
        body["purpose"] = purpose
        body["header"] = header
        body["type"] = type
        
        query = config.MATTERMOST_URL + "/api/v4/channels"
        r = requests.request('POST', query, json=body, headers=headers)
        print(r)
        if not r.ok:
            print(Exception("Error", "query: ", query, ",         r.json() ", r.json()))
            return None
        info = r.json()
        
        return info["id"]
        
    def get_list(self):
        query = config.MATTERMOST_URL + "/api/v4/teams/{team_id:s}/channels".format(team_id=self.team_id)
        r = requests.request('GET', query, headers=headers)
        print(r)
        if not r.ok:
            print(Exception("Error", "query: ", query, ",         r.json() ", r.json()))
            return None
        info = r.json()
        return [(c["id"], c["name"]) for c in info]
    
    def delete(self, channel_id):
        query = config.MATTERMOST_URL + "/api/v4/channels/{channel_id:s}".format(channel_id=channel_id)
        r = requests.request('DELETE', query, headers=headers)
        print(r)
        if not r.ok:
            print(Exception("Error", "query: ", query, ",         r.json() ", r.json()))
            return None
        info = r.json()
        return info
    
    def add_post(self, channel_id, message, headers = headers):                
        post = {
            "channel_id": channel_id,
            "message": message,
            "root_id": None,
            "file_ids": [],
            "props": { }
        }
        query = config.MATTERMOST_URL + "/api/v4/posts"
        r = requests.request('POST', query, json=post, headers=headers)
        print(r)
        if not r.ok:
            print(Exception("Error", "query: ", query, ",         r.json() ", r.json()))
            return None
        info = r.json()
        return info
        

if __name__ == "__main__":
    channel = Channel(team_id = "satzcatq1prftgtfz6c9m5x9my")
    #print(channel.create(name = "est"))
    print(channel.get_list())
    #print(channel.delete(channel_id = 'a79rdehp6ink3brpzwqwdrijjh'))
    #print(channel.add_post(channel_id = 'hq56dis14iyitrbdtedn8sm6ir', message = "ddd"))