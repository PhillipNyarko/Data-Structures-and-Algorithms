from jovian.pythondsa import evaluate_test_cases


def binary_search(lo, hi, condition):
    while lo <= hi:  # as long as we still have elements in the list, we run binary search
        mid = (lo + hi) // 2  # define the middle index value as half of the list
        result = condition(mid)  # call the "test_location" function to locate target value

        if result == 'found':  # return value if it is found
            return mid
        elif result == 'left':  # shrink the cards list search scope to equal one less than the current middle value
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1  # shrink the cards list search scope to equal one more than the current middle value
    return -1  # return -1 if the whole cards list is searched and the value is not found

def recursive_binary_search(nums, target):
    """returns the index position and the value of the target position if found, else returns none"""
    """Begins @ midpoint of list, checks if target is higher/lower, draws first index to previous midpoint +1 repeats"""
    """ This function returns the value of the search to thh previous function that called it"""
    """This function has a logarithmic run time with a a time complexity of O(log(n))"""
    if len(nums) == 0:
        return False
    else:
        midpoint = len(nums)//2
        if nums[midpoint] == target:
            return True
        elif nums[midpoint] < target:
            return recursive_binary_search(nums[midpoint+1:], target)
        else:
            return recursive_binary_search(nums[:midpoint-1], target)

""" The "locate_card" function is used to find the middle index and pass it to the "test_location" function.
If the "test_location" returns found, then the middle has been found, else we alter the list scope
either to the left or the right and begin the search again. If the value isn't found by the time the "lo" bound 
of the list is not less than the "hi" value, then return -1.
Its important to note that by using this while-loop method, the original cards list is never actually modified, but
the scope that is searched through is changed on each loop. Using a while loop is best when we cannot say for sure
just how many iterations there will be before we find our result.
"""


def locate_card(cards, target):  # takes in the middle value, the cards list, and target location

    def condition(mid):
        if cards[mid] == target:  # if the middle number is the target...
            if mid > 0 and cards[mid-1] == target:  # and its left neighbor is not out of bounds and is also the target.
                return 'left'  # the value left of the found index also is the target value
            else:
                return 'found'  # if the value to the left is not also the target then we have found the target
        elif cards[mid] < target:  # return left if the middle number is left of the target
            return 'left'
        else:
            return 'right'  # return right if the middle number is left of the target
    return binary_search(0, len(cards) - 1, condition)  # call binary search


"""
TIME COMPLEXITY: 0(log n)
   with each iteration, the size of the data set gets halved 
"""
#  writing test with sample inputs and outputs ensures that the code behaves the way it should in all cases

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
