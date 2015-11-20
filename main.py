
import random
from collections import Counter

def flip_coin(wang_has_fixed_coin=False):
    if wang_has_fixed_coin:
        return True #heads 
    else:
        return random.randint(1,2) == 1 # regular coin flip 

print("Will Wang Lei die?")

attendees = 22 # number of drink buyers
total_test_cases = 100000 #montocarlo simulation attempts 
threshold_for_death = 11 #shots

test_cases = [sum([flip_coin() for coin_flip in range(attendees)]) for test_case_no in range(total_test_cases)]

death_array = Counter(test_cases)


total_death_odds = sum([0 if drinks < threshold_for_death else total_incidents for drinks, total_incidents in death_array.iteritems()])

total_percent_chance = total_death_odds*100.0/total_test_cases

print("Wang Lei's odds of death are at "+str(total_percent_chance)+"%")
