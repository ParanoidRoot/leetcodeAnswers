#@Time  : 2019/5/16 13:05
#@Author: Root
#@File  : leetcode31.py


class Solution:
    def nextPermutation(self, nums : list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or n == 1 :
            return
        p = n - 1
        while p > 0 and nums[p - 1] >= nums[p] :
            p -= 1
        if not p :
            nums.reverse()
            return
        elif p == n - 1:
            nums[p], nums[p - 1] = nums[p - 1], nums[p]
            return
        else :
            index, value = p - 1, nums[p - 1]
            while p < n and nums[p] > value :
                p += 1
            nums[index], nums[p - 1] = nums[p - 1], nums[index]
            low = index + 1
            high = n - 1
            while low < high :
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
            return


if __name__ == "__main__" :

    nums = [0, 1, 2, 3, 4, 5]
    print(id(nums[1 : ]))
    print(id(nums))




