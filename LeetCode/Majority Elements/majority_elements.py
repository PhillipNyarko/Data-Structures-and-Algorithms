def majority_element(nums):
    frequency_table = {}

    for i in range(len(nums)):
        if nums[i] in frequency_table:
            frequency_table[nums[i]] += 1
        else:
            frequency_table[nums[i]] = 1

    for key in frequency_table:
        if frequency_table.get(key) >= len(nums) / 2:
            return key


print(majority_element([2, 2, 1, 1, 1, 2, 2]))
