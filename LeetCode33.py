#@Time  : 2019/5/26 10:54
#@Author: ParanoidRoot
#@File  : LeetCode33.py


class Solution:
    def binarySearch(self, nums : list, target : int, low, high) -> int :
        if low > high :
            return -1
        mid = (low + high) // 2
        if nums[mid] == target :
            return mid
        elif nums[mid] > target :
            return self.binarySearch(nums, target, low, mid - 1)
        else :
            return self.binarySearch(nums, target, low + 1, high)

    def search(self, nums: list, target: int) -> int:
        n = len(nums)
        if not n :
            return -1
        if n == 1 :
            return 0 if nums[0] == target else -1
        if n == 2 :
            try :
                return nums.index(target)
            except :
                return -1
        # 若个数大于等于三
        low = 0
        high = n - 1
        if target == nums[low] :
            return low
        if target == nums[high] :
            return high
        if nums[low] < nums[high] :
            return self.binarySearch(nums, target, low, high)

        while low != high - 1 :
            mid = (low + high) // 2
            if nums[mid] > nums[low] :
                low = mid
            else :
                high = mid
        last = low
        first = high
        if target > nums[0] :
            return self.binarySearch(nums, target, 1, last)
        else :
            return self.binarySearch(nums, target, first, n - 2)

if __name__ == "__main__" :
    Solution().search([3, 4, 5, 6, 7, 8, 9, 10, -33, -32, -23, -16, -2, -1], 6)