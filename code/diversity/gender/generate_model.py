import os
import random
from string import ascii_lowercase
from sklearn.neural_network import MLPClassifier


def vectorize(s):
    s_vector = [0 for _ in range(26*15)]
    for c in range(len(s)):
        alph_ind = ascii_lowercase.index(s[c])
        s_vector[c*26 + alph_ind] = 1
    return s_vector


with open('{}/name_gender.csv'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
    name_gender = f.read().split()[1:-1]
    males = [vectorize(male.split(',')[0].lower()) for male in name_gender if male.split(',')[1] == 'M']
    females = [vectorize(female.split(',')[0].lower()) for female in name_gender if female.split(',')[1] == 'F']

random.shuffle(males)
random.shuffle(females)

test_male = males[-1000:]
test_female = females[-1000:]

males = males[:16000]
females = females[:16000]

gender_classifier = MLPClassifier()
gender_classifier.fit(males + females, [1 for _ in range(len(males))] + [0 for _ in range(len(females))])


corr = 0
for male in test_male:
    if gender_classifier.predict([male])[0] >= .5:
        corr += 1
print('Male Accuracy: {}'.format(corr/float(1000)))

corr = 0
for female in test_female:
    if gender_classifier.predict([female])[0] <= .5:
        corr += 1
print('Female Accuracy: {}'.format(corr/float(1000)))

import pickle
pickle.dump(gender_classifier, open('{}/gender_classifier.scikit'
                                    .format(os.path.dirname(os.path.realpath(__file__))), 'wb'))