class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        s = 0
        while left < right+1:
            s += self.nums[left]
            left += 1
        return s
        # for i in range(left,(right + 1)):
          # s += self.nums[i]
