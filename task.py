import requests, json, csv

OWNER = "ThomasChuDesigns"
REPO = "pyRPG"

KEYWORDS = {"fix": True}

def main():
    endpoint = requests.get("https://api.github.com/repos/{}/{}/commits".format(OWNER, REPO))
    data = endpoint.json()

    for commit in data:
        print(commit["commit"]["message"])

main()