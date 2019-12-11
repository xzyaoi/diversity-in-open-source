import os
import pickle
from string import ascii_lowercase
from sklearn.neural_network import MLPClassifier

with open('{}/gender_classifier.scikit'.format(os.path.dirname(os.path.realpath(__file__))), 'rb') as f:
    gender_classifier = pickle.load(f)

def classify_gender(s):
    """
    Classify gender based on first name using gender classification model
    :param s: str -> string representing the first name of given candidate
    :return: str -> str corresponding to the binary classification of gender -> 1 male, 0 female
    """
    gender = {1: 'male', 0: 'female'}
    return gender[gender_classifier.predict([_string_vector(s.lower())])[0]]

def _string_vector(s):
    """
    Turn given string into 15x26 vector
    :param s: str -> string representing the first name of given candidate
    :return: list(int) -> 15x26 vector representation of string
    """
    s = s.lower().split(" ")[0]
    s = s[0:15]
    if len(s) > 15:
        raise TypeError('String "{}" too large. len(s) must be <= 15'.format(s))
    s = [c for c in s if c in ascii_lowercase]
    _s_vector = [0 for _ in range(26 * 15)]
    for c in range(len(s)):
        _alpha_ind = ascii_lowercase.index(s[c])
        _s_vector[c * 26 + _alpha_ind] = 1
    return _s_vector
