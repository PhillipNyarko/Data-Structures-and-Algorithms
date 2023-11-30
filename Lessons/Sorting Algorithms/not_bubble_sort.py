# Made independently, not part of Jovian AI Course

from colorama import Fore  # for test cases


def swap(nums, index):
    nums[index], nums[index + 1] = nums[index + 1], nums[index]


def bubble_sort(nums):
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
    'input':  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}, {
    "test case name": "All List Elements Are the Same",
    'input': [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    'output': [-1, -1, -1, -1, -1, -1, -1, -1, -1]
}, {
    "test case name": "Swap Every Element",
    'input': [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 10],
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}, ]


def run_test_cases(tests):
    passed, failed = 0, 0

    for index, dict_key in enumerate(tests):

        test_case_name = dict_key['test case name']
        function_input = dict_key['input']
        expected_output = dict_key['output']
        actual_output = bubble_sort(dict_key['input'])

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
