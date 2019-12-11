import csv
import pandas as pd
'''
#read files
go_list = pd.read_csv('go_repositories.csv', usecols=['name'])
contributions = pd.read_csv('Contributions.csv', usecols=['username', 'reponame'])
contributors = pd.read_csv('Contributors.csv', usecols=['name','location', 'company'])

go_contributors = {}
results = []

for each in go_list.values:
    lc = ''
    company = ''
    #name = ''

    for repo in contributions.values:

        if each == repo[1]:
            for user in contributors.values:
                if repo[0] == user[0]:
                    #name = user[0]
                    #lc = user[1]
                    #company = user[2]
                    go_contributors['reponame'] = repo[1]
                    go_contributors['location'] = user[1]
                    go_contributors['company'] = user[2]
                    results.append(go_contributors)
                    go_contributors = {}

keys = results[0].keys()
with open('go_contributors.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)
'''
#go_contributor = pd.read_csv('go_contributors-na.csv', usecols=['reponame','location'])



with open('go_contributors-na.csv', 'r') as fin, open('go_locations.csv', 'w') as fout:
    #writer = csv.DictWriter(fout, fieldnames = ['reopname', 'location'])
    #writer.writeheader()
    writer = csv.writer(fout)
    for each in csv.reader(fin):
        if type(each[1]) != 'nan':
            print(each)
            writer.writerow(each)

    
    


