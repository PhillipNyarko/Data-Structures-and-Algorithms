# Made independently, not part of Jovian AI Course

from colorama import Fore  # for test cases


def swap(nums, index):
    nums[index], nums[index + 1] = nums[index + 1], nums[index]


def insertion_sort(nums):
    i = 0
    j = 1
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            swap(nums, i)
            while i - j >= 0 and nums[i - j] > nums[i - j + 1]:
                swap(nums, i - j)
                j += 1
            j = 1

        i += 1
    return nums


test_cases = [{
    "test case name": "List Sorted in Descending Order",
    'input': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}, {
    "test case name": "List Already Sorted",
    'input': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}, {
    "test case name": "All List Elements Are the Same",
    'input': [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    'output': [-1, -1, -1, -1, -1, -1, -1, -1, -1]
}, {
    "test case name": "Swap Every Element",
    'input': [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 10],
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}, {
    "test case name": "100 Random Numbers",
    'input': [92, 47, 53, 16, 81, 24, 1, 64, 54, 67,
              78, 3, 26, 95, 68, 85, 4, 74, 55, 40,
              23, 65, 27, 36, 30, 97, 31, 22, 77, 96,
              83, 41, 34, 14, 56, 73, 9, 89, 39, 5,
              50, 32, 70, 91, 69, 42, 59, 76, 8, 13,
              60, 80, 11, 18, 12, 98, 10, 21, 15, 6,
              20, 33, 17, 75, 100, 28, 90, 7, 25, 58,
              29, 88, 79, 45, 63, 38, 37, 52, 46, 71,
              2, 87, 19, 72, 57, 49, 84, 44, 61, 48,
              99, 43, 94, 35, 62, 93, 86, 82, 66, 51,
              ],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
               41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
               51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
               61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
               71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
               81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
               91, 92, 93, 94, 95, 96, 97, 98, 99, 100
               ]
}, {
    "test case name": "All Sorted But one element in the middle",
    'input': [-23, -22, 4, 5, -100, 6, 7, 8, 9, 10],
    'output': [-100, -23, -22, 4, 5, 6, 7, 8, 9, 10]
}, {
    "test case name": "2 Unsorted Elements",
    'input': [1, 0],
    'output': [0, 1]
}, {
    "test case name": "One Element",
    'input': [46],
    'output': [46]
}]


def run_test_cases(tests):
    passed, failed = 0, 0

    for index, dict_key in enumerate(tests):

        test_case_name = dict_key['test case name']
        function_input = dict_key['input']
        expected_output = dict_key['output']
        actual_output = insertion_sort(dict_key['input'])

        if actual_output == expected_output:
            print(f'''{Fore.LIGHTWHITE_EX}
            TEST #{index + 1}
            
            Test Case: {test_case_name}
            Input: {function_input}
            
            Expected Output: {expected_output}
            Actual Output:   {actual_output}
            
            {Fore.GREEN}Test Passed{Fore.LIGHTWHITE_EX}
            -----------------------------------------------------------------------------------
            ''')
            passed += 1
        else:
            print(f'''
            TEST #{index + 1}

            Test Case: {test_case_name}
            Input: {function_input}

            Expected Output: {expected_output}
            Actual Output:   {actual_output}

            {Fore.RED}Test Failed{Fore.LIGHTWHITE_EX}
            -----------------------------------------------------------------------------------
            ''')
            failed += 1

    print(f'''
    # {Fore.GREEN}Passed {Fore.LIGHTWHITE_EX}: {passed}
    # {Fore.RED}Failed {Fore.LIGHTWHITE_EX}: {failed}             
    ''')


run_test_cases(test_cases)
