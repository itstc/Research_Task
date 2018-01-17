from core.mine_commit import get_repository_commits, parse_commits
from core.utils import export_to_csv

def main():
    repo = get_repository_commits('ThomasChuDesigns', 'pyRPG')
    export_to_csv(parse_commits(repo, {'added'}), 'results/test')
    print('csv file created!')

main()