from core.mine_commit import load_commits, is_repository
from core.utils import export_to_csv

def main():
    user = ''
    auth_key = ''
    repo = ''

    user = input('Enter Github Username (optional): ')
    if(user):
        auth_key = input('Enter Github Password or Access Key: ')

    while not is_repository(repo):
        repo = input('Enter repository to mine (:owner/:name): ')

    out = input('Enter where to output file: ')
    data = load_commits(repo, (user, auth_key))
    export_to_csv(data, out)

main()
