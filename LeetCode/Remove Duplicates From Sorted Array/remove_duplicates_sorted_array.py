def remove_duplicates(nums):
    list_length = len(nums)
    pointer = 1
    duplicates = 0

    i = 0  # loop control variable
    while i < list_length - 1:
        if nums[pointer] == nums[i] and pointer != -1:
            duplicates += 1
            if pointer + 1 > list_length - 1:
                pointer = -1
            else:
                pointer += 1
        else:
            before = nums[:i + 1]
            after = nums[i + duplicates + 1:]

            nums.clear()
            nums.extend(before)
            nums.extend(after)

            list_length = len(nums)
            duplicates = 0
            i += 1
            pointer = i + 1

    unique_elements = len(nums)

    return unique_elements, nums


my_list = [3, 3, 3, 6, 6, 7, 7, 8, 8, 8, 9, 20, 20, 21]

print(remove_duplicates(my_list))
