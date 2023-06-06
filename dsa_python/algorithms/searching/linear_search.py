from dsa_python.test_cases import TestCasesChecker, DisplayResults


def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


if __name__ == '__main__':
    test_cases = [
        {'nums': [-1, 0, 3, 5, 9, 12], 'target': 9},
        {'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'target': 10},
        {'nums': [-3, -2, -1, 0, 1, 2, 3], 'target': -3},
        {'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'target': -10}
    ]
    expected_outputs = [
        4,
        9,
        0,
        -2
    ]
    tests_runner = TestCasesChecker(
        test_cases=test_cases, expected_outputs=expected_outputs)

    results = tests_runner.run_test_cases(fn=linear_search)
    print(results)

    dr = DisplayResults(results=results)
    print(dr)

    print("Linear search:")
    # target = 7
    target = 9
    nums = [-1, 0, 3, 5, 9, 12]
    result = linear_search(nums=nums, target=target)
    if result != -1:
        print("Found {} at index {}".format(target, result))
    else:
        print("Didn't find target :(")
