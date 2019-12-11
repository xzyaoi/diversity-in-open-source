import csv
import pandas as pd

repositories = []
with open('repositories.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for r in readCSV:
        if r[2] == "Go":
            repositories.append(r[1])

print(repositories)
df = pd.DataFrame(repositories, columns=["name"])

df.to_csv('./go_repositories.csv')