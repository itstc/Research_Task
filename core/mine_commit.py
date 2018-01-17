import requests

API_URL = "https://api.github.com/repos"

def get_repository_commits(owner, repository):
    # creates a GET request to a url and returns it as a json file
    # url format: https://api.github.com/:owner/:repository/commits

    return (requests.get("{}/{}/{}/commits".format(API_URL, owner, repository))).json()

def parse_commits(data, keywords={'fix'}):
    # param data: json object to parse
    # param keywords: set of all words(lowercase) to flag (default: 'fix')
    # returns list of commits containing keywords in message
    # commit format: {'Commit SHA':'SHA', 'Commit message': 'message'}

    results = []

    for commit in data:
        message = set(commit['commit']['message'].lower().split(' '))

        # if there are keywords in messages then append this commit to results
        if(message & keywords): 
            results.append({
                'Commit SHA': commit['sha'],
                'Commit message': commit['commit']['message']
            })

    return results
