def remove_duplicates(nums):
    list_length = len(nums)
    pointer = 1
    duplicates = 0

    total_duplicates = 0

    i = 0  # loop control variable
    while i < list_length - 1:
        if nums[pointer] == nums[i]:
            duplicates += 1
            pointer += 1
        else:
            nums = nums[:i + 1] + nums[i + duplicates + 1:]
            list_length = len(nums)
            total_duplicates += duplicates
            duplicates = 0
            i += 1
            pointer = i + 1

    unique_elements = len(nums)
    nums = nums + ["_"] * total_duplicates

    return unique_elements, nums


my_list = [3, 3, 3, 6, 6, 7, 7, 8, 8, 8, 9, 20, 20, 21]

print(remove_duplicates(my_list))
