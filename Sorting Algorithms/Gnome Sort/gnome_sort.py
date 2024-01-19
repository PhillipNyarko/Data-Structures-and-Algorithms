# Made independently, not part of Jovian AI Course

""" I made a sorting algorithm while "away" on a "trip" and when I got back turns out it was just something called
gnome sort lol """

import copy
import os
import time

RED = "\u001b[31m"
YELLOW = "\u001b[33m"
GREEN = "\u001b[32m"
WHITE = "\033[1;37m"
BLUE = "\u001b[34m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"


def swap(nums, index):
    nums[index], nums[index + 1] = nums[index + 1], nums[index]


def gnome_sort(nums):
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

    for i, test in enumerate(tests):
        test_case_name = test["test case name"]
        function_input = test['input']
        expected_output = test['output']
        actual_output = gnome_sort(copy.deepcopy(function_input))

        print(f''' {WHITE}
        TEST #{i + 1}

              Test Case: {test_case_name}
              Input: {function_input}

              Expected Output: {expected_output}
              Actual Output:   {actual_output}
        ''')

        if actual_output == expected_output:
            print(f"              {GREEN}TEST PASSED{WHITE}")
            passed += 1
        else:
            print(f"              {RED}TEST FAILED{WHITE}")
            failed += 1

        print("-" * 1000)  # cool/unnecessary way to print 100 char line. This way you don't have to count or adjust

    print(GREEN + "Passed" + WHITE + ": " + str(passed))
    print(RED + "Failed" + WHITE + ": " + str(failed))


def run_visualisation(nums):

    nums = [i//3 for i in nums]
    nums_copy = nums.copy()
    gnome_sort(nums_copy)
    biggest_number = nums_copy[-1]

    # make sure your $ is in order
    def draw_columns(index, color, finishing_animation=False, last_frame_of_finishing_animation=False):
        for i in range(biggest_number, 0, -1):
            for j in range(len(nums)):
                if nums[j] >= i:
                    if finishing_animation:
                        if last_frame_of_finishing_animation:
                            print(color + " x " + WHITE, end="")
                        elif j <= index:
                            print(color + " x " + WHITE, end="")
                        else:
                            print(" x ", end="")
                    else:
                        if j == index:
                            print(color + " x " + WHITE, end="")
                        else:
                            print(" x ", end="")
                else:
                    print("   ", end="")
            print()  # new line
        time.sleep(0.05)
        os.system('cls')
        os.system('clear')

    current_index = 0
    pointer = 1

    while current_index < len(nums) - 1:
        if nums[current_index] > nums[current_index + 1]:
            swap(nums, current_index)
            draw_columns(current_index, GREEN)
            while current_index - pointer >= 0 and nums[current_index - pointer] > nums[current_index - pointer + 1]:
                swap(nums, current_index - pointer)
                draw_columns(current_index - pointer, RED)
                pointer += 1
            pointer = 1

        current_index += 1

    for i in range(len(nums)):
        if i < len(nums) - 1:
            draw_columns(i, GREEN, finishing_animation=True)
        else:
            draw_columns(i, GREEN, finishing_animation=True, last_frame_of_finishing_animation=True)


run_visualisation([92, 47, 53, 16, 81, 24, 1, 64, 54, 67,
                   78, 3, 26, 95, 68, 85, 4, 74, 55, 40,
                   23, 65, 27, 36, 30, 97, 31, 22, 77, 96,
                   83, 41, 34, 14, 56, 73, 9, 89, 39, 5])
