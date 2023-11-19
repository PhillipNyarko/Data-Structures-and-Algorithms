from jovian.pythondsa import evaluate_test_cases


def rotate(nums, rotations):  # this function "rotates" a given list, and is only used to fill the test cases
    for i in range(rotations):  # preform the rotation steps a specified number of times
        last = nums[-1]  # take the last number of the list and store it temporarily
        rest = nums[:len(nums)-1]  # take every element but the last element and store it temporarily
        nums.clear()  # clear the number list
        nums.append(last)  # put the last element first
        for j in range(len(rest)):  # use a for loop to append the rest of the elements after the original last element
            nums.append(rest[j])
    return nums  # return the new number array


"""
be wary of preforming operations/modifications on a list without making a copy and using the copy 
as it can have unintended consequences
"""


def count_rotations_binary(nums):  # essentially, return the index of the smallest number in the list
    low = 0  # this is a "pointer" of sorts that points to the lowest index that will be looked at in the binary search
    high = len(nums) - 1  # this is also a "pointer" that points to the highest part that will be searched

    # to look through the whole list, we must keep looking until the high value is less than the low
    # This allows the function to run even when the list has one element, and it stops after the list is empty

    while low <= high:
        middle_index = (low + high) // 2  # this method because it accounts for a change in the "low" or "high" value
        middle_number = nums[middle_index]  # get the value of the number at the middle index.
        if middle_number < nums[middle_index - 1] or len(nums) == 1:  # middle number < the number to the left of it?
            return middle_index  # return that index, because the number at that index is the smallest in the list
        elif middle_number < nums[-1]:  # if the middle number is less than the last number in the list
            high = middle_index - 1  # move the high index pointer to the value of the middle index -1
        else:
            low = middle_index + 1  # move the low index pointer to the value of the middle index +1
    return -1  # return negative 1 if the value is not in the list.


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

evaluate_test_cases(count_rotations_binary, tests)
