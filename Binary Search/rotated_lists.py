from jovian.pythondsa import evaluate_test_cases


def is_sorted(nums):  # use a for loop to check if the list is sorted
    def rotate():
        last = nums[-1]
        nums_copy = nums.copy()
        nums.clear()
        nums.append(last)
        for j in range(len(nums_copy) - 1):
            nums.append(nums_copy[j])
        # print(nums)

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            rotate()
            return False
    return True


def count_rotations(nums):
    rotations = - 1 if len(nums) > 1 else 0
    while not is_sorted(nums):
        rotations += 1
    return rotations


# write test cases
tests = [{
    'input': {  # basic, normative input
        'nums': [5, 6, 9, 0, 2, 3, 4]
    },
    'output': 3
}]

evaluate_test_cases(count_rotations, tests)
