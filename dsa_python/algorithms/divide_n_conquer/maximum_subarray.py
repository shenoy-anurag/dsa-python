import math


def max_cross_subarray(nums, low, mid, high):
    sum_left = float("-inf")
    sum = 0
    max_left = None
    for i in range(mid, low, -1):
        sum += nums[i]
        if sum > sum_left:
            sum_left = sum
            max_left = i
    sum_right = float("-inf")
    sum = 0
    max_right = None
    for i in range(mid + 1, high):
        sum += nums[i]
        if sum > sum_right:
            sum_right = sum
            max_right = i
    return max_left, max_right, sum_left + sum_right


def max_subarray(nums, low, high):
    if high == low:
        return (low, high, nums[low])
    else:
        mid = (low + high) // 2
        # sub-array from low to mid:
        low_left, high_left, sum_left = max_subarray(nums, low, mid)
        # sub-array from mid to high:
        low_right, high_right, sum_right = max_subarray(nums, mid + 1, high)
        # cross-sub-array:
        low_cross, high_cross, sum_cross = max_cross_subarray(nums, low, mid, high)
        if sum_left >= sum_right and sum_left >= sum_cross:
            return (low_left, high_left, sum_left) 
        elif sum_right >= sum_left and sum_right >= sum_cross:
            return (low_right, high_right, sum_right)
        else:
            return (low_cross, high_cross, sum_cross)


if __name__ == '__main__':
    nums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    print(max_subarray(nums=nums, low=0, high=len(nums) - 1))
    
