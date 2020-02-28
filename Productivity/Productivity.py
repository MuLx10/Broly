import os
import json
import requests
import datetime
import config
from collections import defaultdict
import Report.ContributionReport

dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = '/'.join(dir_path.split('/')[:-2])



class PRsProductivity(Report.ContributionReport.ContributionReport):
    """docstring for PRsProductivity"""
    def __init__(self, org_name):
        super(PRsProductivity, self).__init__(org_name)
        self.headers = {
            'Authorization': 'token ' + config.GH_API_KEY
        }
        self.projects = []

    def get_pr_data(self, project, since):
        query = "https://api.github.com/repos/{}/pulls".format(project)
        prs = self.fetch_all_pull_requests(query, since=since, headers=self.headers)
        
        # Trim out of date pull requests
        while(True):
            if len(prs) == 0:
                break
            if prs[-1]['created_at'] < since:
                prs.pop()
            else:
                break
                
        return prs
    
    
    def run(self, dT = 1):
        T = datetime.date.today()
        dT = datetime.timedelta(days=dT)
        
        since = str(T-dT).split(' ')[0]+'T00:00:00Z'
        until = str(T).split(' ')[0]+'T00:00:00Z'
        data = defaultdict(dict)
        for project in self.projects:
            prs_data = self.get_pr_data(project, since)
            for pr in prs_data:
                data[project][pr['number']] = { 
                    'title':pr['title'], 
                    'state':pr['state'],
                    'created_at': pr['created_at'], 
                    'closed_at': pr['closed_at'], 
                    'merged_at':pr['merged_at'],
                    'requested_reviewers':[x['login'] for x in pr['requested_reviewers']],
                    'labels': [x['name'] for x in pr['labels']]}
        return data

def main(org_name, projects):
    pd = PRsProductivity(org_name)
    pd.add_project(projects = projects)
    return pd.run()
    
    
if __name__ == "__main__":
    print(main('mattermost', ['mattermost-mobile']))