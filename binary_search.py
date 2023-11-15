from colorama import Fore  # colors for tests
from jovian.pythondsa import evaluate_test_cases


"""QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing
order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card
containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card."""

""" 1. There is a series of cards sorted in descending order. There is a target card with a given number on it.
    find the card while checking as few cards as possible.
    2a. example input -> cards = [9, 8, 7, 6, 5, 4, 3,] , target_card = 5  (a list of numbers and a target card)
    2b. example output -> " The card "5" is found at index 4 " (index of the target card)
    3. Create a function called "binary_search" that iterates over the a given input list.
             use a "for-loop" for iteration, 
             start iteration from the middle index if the input is odd, 
             start iteration from the index that corresponds to the length of the list / 2 if the input list is even
             because the input is sorted, 
             if the initial number is greater than the target, get rid of every number before that number and that.
"""

""" BRUTE FORCE SIMPLE SOLUTION
1. if the target card is not within the cards list, return -1
2. else, go through each element of the cards list and compare the value with the target
3. if the value == the target value, return the current index"""


def locate_card(cards, target):
    if target not in cards:
        return -1
    else:
        for i in range(len(cards)):
            if cards[i] == target:
                return i


# writing test with sample inputs and outputs ensures that the code behaves the way it should in all cases
tests = [{  # target occurs in the middle
    'input': {
        "cards": [13, 11, 10, 7, 4, 3, 1, 0],
        "target": 7
    },
    "output": 3
}, {  # target is the first element
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'target': 1
    },
    'output': 6
}, {  # target is the last element
    'input': {
        'cards': [4, 2, 1, -1],
        'target': 4
    },
    'output': 0
}, {
    'input': {  # cards contains just one element, target
        'cards': [3, -1, -9, -127],
        'target': -127
    },
    'output': 3
}, {  # cards does not contain target
    'input': {
        'cards': [6],
        'target': 6
    },
    'output': 0
}, {  # cards is empty
    'input': {
        'cards': [],
        'target': 7
    },
    'output': -1
}, {  # numbers can repeat in cards
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'target': 3
    },
    'output': 7
}, {  # target occurs multiple times
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'target': 6
    },
    'output': 2}]


evaluate_test_cases(locate_card, tests)
