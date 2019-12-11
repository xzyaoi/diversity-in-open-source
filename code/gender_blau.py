import csv
import pandas as pd

go_user_gender_list = pd.read_csv('go_repo_gender.csv',usecols=['reponame', 'male', 'female'])

go_blau = {}
results = []

for each in go_user_gender_list.values:
    go_blau['reponame'] = each[0]
    male = each[1]
    female = each[2]

    n = male + female
    k = 2
    
    if n != 0: 

        p_male = (male/n)
        p_female = (female/n)
        square_p_male = p_male*p_male
        square_p_female = p_female*p_female
        b = square_p_male + square_p_female
        B = 1 - b

        a = n - k*int(n/k)
        square_n = n*n
        b_max_molecule = square_n + (a*(a-k))

        if b_max_molecule == 0:
           go_blau['blau_index'] = B
        else: 
            B_max = (b_max_molecule)/(k*square_n)
            B_n = B / B_max
            go_blau['blau_index'] = B_n
        
        results.append(go_blau)

    go_blau = {}

print(results)

keys = results[0].keys()
with open('go_gender_blau.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)