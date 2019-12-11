import csv
import pandas as pd

#read files
go_list = pd.read_csv('go_repositories.csv', usecols=['name'])
contributions = pd.read_csv('Contributions.csv', usecols=['username', 'reponame'])
contributors = pd.read_csv('Contributors.csv', usecols=['name','gender'])

go_gender = {}
results = []


for each in go_list.values:
    male = 0
    female = 0
    
    go_gender['reponame'] = each[0]
    
    for repo in contributions.values:
        
        if each == repo[1]:
            for user in contributors.values:
                if repo[0] == user[0]:
                    if user[1] == "male":
                        male += 1
                    elif user[1] == "female":
                        female += 1              
        go_gender['male'] = male
        go_gender['female'] = female
    results.append(go_gender)
    go_gender = {}
   


keys = results[0].keys()
with open('go_repo_gender.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)
                

     
