"""
    Insertion Sort

    Algorithm
    ---------
    insertionSort(array)
    mark first element as sorted
    for each unsorted element X
        'extract' the element X
        for j <- lastSortedIndex down to 0
        if current element j > X
            move sorted element to the right by 1
        break loop and insert X here
    end insertionSort

"""


def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1

        nums[j + 1] = key
    return nums


if __name__ == '__main__':
    nums = [7, 3, 7, 72, 45, 852, 56, 8, 2, 9, 0]
    print(insertion_sort(nums))

    from dsa_python.test_cases import run_all_test_cases, check_all_passed, message_all_passed

    test_cases = [
        {'nums': [7, 3, 7, 72, 45, 852, 56, 8, 2, 9, 0]},
        {'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
        {'nums': [-77, -74, -41, 98, -35, -94, 44, 29, -99, 24, 84, -50, -48, 24, 7]}, 
        {'nums': [-53, 23, 23, 40, -83, -38, 41, 71, -87, -52, 78, -68, 61, -41, 53, -91, -2, -50]}, 
        {'nums': [58, -82, -82, 48, 75]}, 
        {'nums': [69, -50, -45, 76, 70, -86, 12, -7, 5, 78]}, 
        {'nums': [52, -74, 47, -72, 20, -70]}
    ]
    expected_outputs = [
        [0, 2, 3, 7, 7, 8, 9, 45, 56, 72, 852],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [-99, -94, -77, -74, -50, -48, -41, -35, 7, 24, 24, 29, 44, 84, 98],
        [-91, -87, -83, -68, -53, -52, -50, -41, -38, -2, 23, 23, 40, 41, 53, 61, 71, 78],
        [-82, -82, 48, 58, 75],
        [-86, -50, -45, -7, 5, 12, 69, 70, 76, 78],
        [-74, -72, -70, 20, 47, 52]
    ]
    dr = run_all_test_cases(
        fn=insertion_sort, test_cases=test_cases,
        expected_outputs=expected_outputs, strict_checking=True
    )
    print(dr)

    all_passed = check_all_passed(dr)
    if all_passed:
        print()
        print(message_all_passed())
