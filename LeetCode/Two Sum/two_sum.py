def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum([1, 2, 3, 4, 5], 4))  # Expected output [0, 2]

print(two_sum([3, 2, 4], 6))  # Expected output [1, 2]

print(two_sum([3, 3], 6))  # Expected output [0, 1]
