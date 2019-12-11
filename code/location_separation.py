import csv
import pandas as pd
import math
from geopy.distance import geodesic 


#read files
go_contributors = pd.read_csv('go_contributors-na.csv', usecols=['reponame','location'])
geo_matrix = pd.read_csv('output-2015.csv', usecols=['formatted_address','latitude','longitude'])

'''
def count_dis(each):
    la_total = 0
    lo_total = 0
    count = 0
    for node in geo_matrix.values:
            if node[0] == each[1]:
                la_total += node[1]
                lo_total += node[2]
                count += 1
                #print(count)
            else:
                pass
    return count, la_total, lo_total

current_repo = ''
la_total = 0
lo_total = 0
count = 0
repo_distance = {}
results = []

for each in go_contributors.values:
    
    if not current_repo:
        current_repo = each[0]
        c, la, lo = count_dis(each)
        count += c
        la_total += la
        lo_total += lo
    elif current_repo != each[0]:
        #print(current_repo)
        #print(count)
        repo_distance['reponame'] = current_repo
        repo_distance['n'] = count
        repo_distance['la_total'] = la_total
        repo_distance['lo_total'] = lo_total
        results.append(repo_distance)
        print(results)
        count = 0
        la_total = 0
        lo_total = 0
        repo_distance = {}
        current_repo = each[0]
        c, la, lo = count_dis(each)
        count += c
        la_total += la
        lo_total += lo
    elif current_repo == each[0]:
        c, la, lo = count_dis(each)
        count += c
        la_total += la
        lo_total += lo

keys = results[0].keys()
with open('go_distance.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)
 '''       
def get_average(distance, reponame):
    la_avg = 0
    lo_avg = 0
    n = 0
    for dis in distance.values:
        if reponame == dis[0] and dis[1] != 0:
            la_avg = dis[2]/dis[1]
            lo_avg = dis[3]/dis[1]
            n = dis[1]
    return la_avg, lo_avg, n

def count_gap(each, la_avg, lo_avg):
    gap = 0
    point = (la_avg, lo_avg)
    for node in geo_matrix.values:
            if node[0] == each[1]:
                current_point = (node[1], node[2])
                gap = (geodesic(point, current_point).km)
            else:
                pass
    return gap*gap

distance = pd.read_csv('go_distance.csv', usecols=['reponame','n','la_total','lo_total'])

current_repo = ''
la_avg = 0
lo_avg = 0
count = 0
n = 0
repo_distance = {}
results = []
for each in go_contributors.values:
    
    if not current_repo:
        current_repo = each[0]
        la_avg, lo_avg, n = get_average(distance, current_repo)
        gap = count_gap(each, la_avg, lo_avg)
        count += gap
    elif current_repo != each[0]:
        if n != 0:
            sd = math.sqrt(count/n)
            repo_distance['reponame'] = current_repo
            repo_distance['sd'] = sd
            results.append(repo_distance)
            #print(results)
        count = 0
        la_total = 0
        lo_total = 0
        n = 0
        repo_distance = {}
        current_repo = each[0]
        la_avg, lo_avg, n = get_average(distance, current_repo)
        gap = count_gap(each, la_avg, lo_avg)
        count += gap
        
    elif current_repo == each[0]:
        gap = count_gap(each, la_avg, lo_avg)
        count += gap


print("part 1 finish!")

keys = results[0].keys()
with open('go_location_separation.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)


     
