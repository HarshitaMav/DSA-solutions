class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        brk = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                brk = i
                break
        left = len(nums)-1
        while left > brk:
            if nums[left] > nums[brk]:
                break
            left -= 1
        if left != brk:
            nums[brk], nums[left] = nums[left], nums[brk]
        else:
            nums[brk], nums[-1] = nums[-1], nums[brk]
        i = brk + 1
        j = len(nums) - 1
        while i <= j:
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                j -= 1