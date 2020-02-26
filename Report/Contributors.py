import requests
import os
from base64 import encodestring as base64
import config
import pickle
from pathlib import Path


headers = {
    'Authorization': 'token ' + config.GH_API_KEY
}

def get_full_name(username):
    url = "https://api.github.com/users/"+username
    r=requests.get(url, headers=headers).json()
    try:
        return str(r['name']).encode('utf-8'), str(r['avatar_url']).encode('utf-8')
    except Exception as e:
        print(e)
        return None, None

def get_contributors(org_name, project_name, nameRequired=False):
    contributors_list_file = 'files/contributors_list'+str(org_name)+str(project_name)
   
    if Path(contributors_list_file).is_file():
        with open (contributors_list_file, 'rb') as fp:
            contributors_list = pickle.load(fp)
        return contributors_list
   
    contributors_usernames = list()
    page_count = 1
    while True:
        url = "https://api.github.com/repos/"+org_name+'/'+project_name+"/contributors?page="+str(page_count)
        contributors = r=requests.get(url,headers=headers)
        if contributors != None and contributors.status_code == 200 and len(contributors.json()) > 0:
            contributors_usernames = contributors_usernames + contributors.json()
            break
        else:
            break
        page_count = page_count + 1
    contributors_usernames = list(map(lambda x: x['login'],contributors_usernames))        
   
    contributors_list = []
    for username in contributors_usernames:
        #print(username)
        try:
            fullname, url = (None, None) if not nameRequired else get_full_name(username) 
            contributors_list.append([str(username),str(fullname), str(url)])
        except Exception as e:
            pass

    with open(contributors_list_file, 'wb') as fp:
        pickle.dump(contributors_list, fp)
    return contributors_list
    
    
if __name__ == '__main__':
    print(get_full_name('mulx10'))
    org_name = 'mattermost'
    project_name = 'mattermost-mobile'
    print(get_contributors(org_name, project_name))