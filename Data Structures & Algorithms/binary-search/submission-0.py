class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, m, r = 0, len(nums)//2, len(nums) - 1
        while l <= r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[m] < target:
                l = m + 1
                m = l + ((r-l)//2)
            elif nums[m] > target:
                r = m - 1
                m = l + ((r-l)//2)
            else:
                return m
        return -1