import csv
import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

#read files
go_list = pd.read_csv('go_repositories.csv', usecols=['name'])
contributions = pd.read_csv('Contributions.csv', usecols=['username', 'reponame'])
contributors = pd.read_csv('Contributors.csv', usecols=['name','location'])

#Geocoding
locator = Nominatim(user_agent='myGeocoer', timeout=3)

go_locations = {}
results = []
with open('go_location_average.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames = ["reopname", "n", "la_total", "lo_total"])
    writer.writeheader()
    for each in go_list.values:
        #print(each)
        count = 0
        dis_la = 0
        dis_lo = 0
        for repo in contributions.values:
            #print(repo[1])
            if each == repo[1]:
                #print(each[0])
                #print(repo[1])
                #print("==============================")    
                for location in contributors.values:
                    coordinate = ''
                    if repo[0] == location[0]:
                        if type(location[1])!=float:
                            count += 1
                            try:
                                coordinate = locator.geocode(location[1])
                            except GeocoderTimedOut as e:
                                print("Error: geocode failed on input")
                            #print(location[1])
                            #print('Latitude = {}, Longitude = {}'.format(coordinate.latitude, coordinate.longitude))
                            #print(coordinate)
                            #print(type(coordinate))
                            if coordinate:
                                dis_la += coordinate.latitude
                                dis_lo += coordinate.longitude
                                #print(dis_la)
                        time.sleep(1.1)
            go_locations['reponame'] = repo[1]
            go_locations['n'] = count
            go_locations['la_total'] = dis_la
            go_locations['lo_total'] = dis_lo
        results.append(go_locations)
        print(repo[1]+','+count+','+dis_la+','+dis_lo)
        f.write(repo[1]+','+count+','+dis_la+','+dis_lo)
        f.write("\n")
        go_locations = {}
'''
keys = results[0].keys
with open('go_location_average.csv', 'w') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)
'''







        
