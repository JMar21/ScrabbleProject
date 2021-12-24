from collections import Counter
from random import shuffle, choice
LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
COUNT = [9,2,2,4,12,2,3,2,9,2,2,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]
bag = list(Counter(dict(zip(LETTERS,COUNT))).elements())
shuffle(bag)

def print_bag():
    for i in bag:
        print(i)
def draw():
    return choice(bag)

