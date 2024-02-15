def check_for_duplicates(nums):
    frequency_table = {}
    for i in nums:
        if i not in frequency_table:
            frequency_table[i] = 1
        else:
            return True
    return False

print(check_for_duplicates([2,2]))
