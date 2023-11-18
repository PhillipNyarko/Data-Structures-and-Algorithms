from jovian.pythondsa import evaluate_test_cases


def rotate(nums, rotations):
    for i in range(rotations):
        last = nums[-1]
        rest = nums[:len(nums)-1]
        nums.clear()
        nums.append(last)
        for j in range(len(rest)):
            nums.append(rest[j])
    return nums


def count_rotations(nums):
    pass


# write test cases
tests = [{
    'input': {  # length of 10 rotated 3 times
        'nums': rotate([1, 2, 3, 4, 5, 6, 7, 8], 3)
    },
    'output': 3
}, {
    'input': {  # length of 8 rotated 5 times
        'nums': rotate([1, 2, 3, 4, 5, 6, 7, 8], 5)
    },
    'output': 5
}, {
    'input': {  # rotated just once
        'nums': rotate([1, 2, 3, 4, 5, 6, 7, 8], 1)
    },
    'output': 1
}, {
    'input': {  # rotated n-1 times, where n is the length of the list
        'nums': rotate([1, 2, 3, 4, 5, 6, 7, 8], 7)
    },
    'output': 7
}, {
    'input': {  # rotated n times, where n is the length of the list
        'nums': rotate([1, 2, 3, 4, 5, 6, 7, 8], 8)
    },
    'output': 0
},  {
    'input': {  # rotated n + 1 times, where n is the length of the list
        'nums': rotate([i for i in range(100)], 101)
    },
    'output': 1
}, {
    'input': {  # not rotated at all
        'nums': [1, 2, 3, 4, 5, 6]
    },
    'output': 0
}, {
    'input': {  # one element
        'nums': [1]
    },
    'output': 0
}, {
    'input': {  # empty list
        'nums': []
    },
    'output': -1
}]

evaluate_test_cases(count_rotations, tests)
