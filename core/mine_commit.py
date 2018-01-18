import requests

start_page = "https://api.github.com"

def load_commits(repo, authData = None, keywords=['fix'], page = 0):
    # load all commits with keywords found in messages
    # param repo: :owner/:repository_name
    # param authData: tuple(token, 'type')
    # returns list({'Commit SHA':'SHA', 'Commit message': 'message'})

    buffer = requests.get("{}/repos/{}/commits?page={}&per_page=100".format(start_page, repo, page), auth = authData)
    if(buffer.status_code != 200 or not buffer.json()): # base case request is invalid
        return []
    
    results = filter_commits(buffer.json(), keywords)
    
    return results + load_commits(repo, authData, keywords, page + 1)

def parse_commit(data):
    # param commit: BeautifulSoup Object to be parsed
    # returns {'Commit SHA':'SHA', 'Commit message': 'message'}

    return {
        'Commit SHA': data['sha'],
        'Commit message': str(data['commit']['message'].encode('utf-8'))[1:]
    }

def filter_commits(data, keywords=['fix']):
    # param data: JSON request object
    # param keywords: set of all words(lowercase) to flag (default: 'fix')
    # returns list of commits containing keywords in message
    # commit format: {'Commit SHA':'SHA', 'Commit message': 'message'}

    results = []

    for commit in data:
        message = commit['commit']['message'].lower()
        for key in keywords:
            if(key in message):
                results.append(parse_commit(commit))
                break

    return results

def is_repository(repo):
    # checks if request sends back an OK status code
    return requests.get("{}/repos/{}".format(start_page, repo)).status_code == 200
