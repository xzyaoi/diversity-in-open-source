import csv
import os
from diversity.gender.gender_classifier import classify_gender

class Model(object):
    def __init__(self):
        self.data = []
        self.fieldnames = []

    def WriteHeader(self):
        with open(self.__class__.__name__+'.csv', mode='a+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writeheader()

class Repositories(Model):
    def __init__(self):
        super(Repositories).__init__()
        self.fieldnames = ['name', 'language',
                           'star_count', 'fork_count', 'owner',
                           'size', 'updated_at', 'created_at']

    def Add(self, name, language, star_count, fork_count, owner, size, updatedAt, createdAt):
        self.data.append({
            "name": name,
            "language": language,
            "star_count": star_count,
            "fork_count": fork_count,
            "owner": owner,
            "size": size,
            "updated_at": updatedAt,
            "created_at": createdAt
        })
        with open('repositories2.csv', mode='a+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writerow({
                "name": name,
                "language": language,
                "star_count": star_count,
                "fork_count": fork_count,
                "owner": owner,
                "size": size,
                "updated_at": updatedAt,
                "created_at": createdAt
            })

class Contributions(Model):
    def __init__(self):
        self.fieldnames = ['username', 'reponame',
                            'times']
        self.data = []
    
    def Add(self, username, reponame, times):
        with open(self.__class__.__name__+'.csv', mode='a+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writerow({
                "username": username,
                "reponame": reponame,
                "times": times,
            })

class Contributors(Model):
    def __init__(self):
        self.fieldnames = ['name', 'gender', 'location',
                           'company','email']
        self.data = []

    def Add(self, name, location, company, email):
        self.data.append(name)
        # predict gender by name
        gender = classify_gender(name)
        with open(self.__class__.__name__+'.csv', mode='a+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writerow({
                "name": name,
                "gender": gender,
                "location": location,
                "company": company,
                "email": email
            })
    
    def IsExists(self, username):
        if username in self.data:
            return True
        else:
            return False