from github import Github

def FetchAllRepositories(min_star=1000, active_contributors=5):
    g = Github("user", "apassword")