def two_sum(nums, target):
    for i in nums:
        if i > target:
            nums.remove(i)

    hash_map = {}

    for index, value in enumerate(nums):
        difference = target - value
        if (difference) in hash_map:
            return [hash_map[difference], index]
        hash_map[value] = index 

print(two_sum([1, 2, 3, 4, 5], 4))  # Expected output [0, 2]

print(two_sum([3, 2, 4], 6))  # Expected output [1, 2]

print(two_sum([3, 3], 6))  # Expected output [0, 1]
