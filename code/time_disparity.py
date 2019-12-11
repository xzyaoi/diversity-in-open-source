import csv 
import math
import pandas as pd

go_list = pd.read_csv('go_repositories.csv', usecols=['name'])
contributions = pd.read_csv('Contributions.csv', usecols=['reponame','times'])
'''
go_times = {}
results = []
for each in go_list.values:
    count = 0
    time_total = 0
    for repo in contributions.values:
        if each[0] == repo[0]:
            count += 1
            time_total += repo[1]
    if count != 0:
        go_times['reponame'] = each[0]
        go_times['time_avg'] = time_total/count
        go_times['n'] = count
        results.append(go_times)
        #print(results)
        go_times = {}

keys = results[0].keys()
with open('go_times.csv','w') as output_file:
    writer = csv.DictWriter(output_file, keys)
    writer.writeheader()
    writer.writerows(results)


'''

times = pd.read_csv('go_times.csv', usecols=['reponame','time_avg','n'])

def get_times_avg(times, reponame):
    count = 0
    time_avg = 0
    for node in times.values:
        if node[0] == reponame and node[2] != 0:
            count = node[2]
            time_avg = node[1]
    
    return count, time_avg


repo_times = {}
results_cov = []
for each in go_list.values:
    count = 0
    time_avg = 0
    gap_total = 0
    for repo in contributions.values:
        if repo[0] == each[0]:
            count, time_avg = get_times_avg(times,each[0])
            gap = repo[1] - time_avg
            square_gap = gap*gap
            gap_total += square_gap
    
    if count != 0:
        cov_molecule = math.sqrt(gap_total/count)
        cov = cov_molecule/time_avg
        repo_times['reponame'] = each[0]
        repo_times['coefficient_of_variation'] = cov
        results_cov.append(repo_times)
        #print(repo_times)
    
    repo_times = {}


keys = results_cov[0].keys()
with open('go_time_disparity.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results_cov)



