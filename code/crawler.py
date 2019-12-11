import os
from github import Github
from model import Repositories, Contributions, Contributors
from tqdm import tqdm
import time
import csv
# Global
github_client = Github(os.environ['GITHUB_ACCESS_TOKEN'])


def FetchAllInterestedRepositories(min_star=1000, active_contributors=10, max_star=10000):
    repositories = Repositories()
    # repositories.WriteHeader()
    pojo_repositories = github_client.search_repositories(
        query='stars:'+str(min_star)+'..'+str(max_star))
    for each in tqdm(pojo_repositories):
        repositories.Add(
            each.full_name, 
            each.language,
            each.stargazers_count,
            each.forks_count,
            each.owner.name,
            each.size,
            each.updated_at,
            each.created_at)
        # Sleep for a while to avoid ratelimit
        time.sleep(0.5)

def _fetch_all_repositories():
    """
    step = 10
    for i in range(1000):
        max_star = 10000 - i * step
        min_star = 10000 - (i+1) * step
        FetchAllInterestedRepositories(min_star=min_star, max_star=max_star)
    """
    FetchAllInterestedRepositories(min_star=2500, max_star=2668)


def _fetch_all_contributors():
    # =====
    # Read all Repositories
    # =====
    repositories = []
    with open('go_repositories.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for r in readCSV:
            repositories.append(r[1])
    # =====
    # Analyse Contributing Data
    # =====
    repositories = repositories[1018:]
    contributors = Contributors()
    contribution = Contributions()
    contributors.WriteHeader()
    contribution.WriteHeader()
    for each in tqdm(repositories):
        repo = github_client.get_repo(each)
        pojo_contributors = repo.get_contributors()
        for each_contributor in pojo_contributors:
            if(each_contributor.name):
                if each_contributor.contributions >= 5:
                    contribution.Add(each_contributor.name, each, each_contributor.contributions)
                    if not contributors.IsExists(each_contributor.name):
                        contributors.Add(each_contributor.name, 
                                        each_contributor.location, 
                                        each_contributor.company, 
                                        each_contributor.email)
                        time.sleep(1.2)

if __name__ == "__main__":
    _fetch_all_contributors()
    #_fetch_all_repositories()
