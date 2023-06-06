import math


def binary_search(nums, target, low, high):
    "Binary search as a standalone recursive function"
    if high >= low:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binary_search(nums, target, low, mid - 1)
        else:
            return binary_search(nums, target, mid + 1, high)
    return -1


class BinarySearch:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.N = len(nums)

    def binary_search(self, target, low, high):
        if high >= low:
            mid = low + (high - low) // 2

            mid_num = self.nums[mid]
            if target > mid_num:
                return self.binary_search(target, mid + 1, high)
            elif target < mid_num:
                return self.binary_search(target, low, mid - 1)
            else:
                return mid
        return -1

    def loop_binary_search(self, target):
        """ Non-recursive version """
        l = 0
        r = self.N - 1
        n = math.ceil(math.sqrt(r + 1))
        for _ in range(n):
            if r >= l:
                mid = l + (r - l) // 2

            mid_el = self.nums[mid]
            if target > mid_el:
                l = mid + 1
            elif target < mid_el:
                r = mid - 1
            else:
                return mid
        return -1

    def search(self, target: int) -> int:
        return self.binary_search(target, 0, self.N - 1)
        # return self.loop_binary_search(target)


if __name__ == '__main__':
    print("Using binary search class:")
    # target = 7
    target = 9
    nums = [-1, 0, 3, 5, 9, 12]
    b_search = BinarySearch(nums=nums)
    idx = b_search.search(target)
    if idx != -1:
        print("Found {} at index {}".format(target, idx))
    else:
        print("Didn't find target :(")
    
    print("Using binary search standalone function:")
    nums = [1,2,3,4,5,6,7,8,9,10,11,12]
    target = 12
    # target = 1
    # target = 15
    idx = binary_search(nums, target, 0, len(nums) - 1)
    if idx != -1:
        print("Found {} at index {}".format(target, idx))
    else:
        print("Didn't find target :(")
