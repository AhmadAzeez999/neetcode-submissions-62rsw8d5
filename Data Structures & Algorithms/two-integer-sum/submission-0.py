class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapOfPrev = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapOfPrev:
                return [mapOfPrev[diff], i]
            mapOfPrev[n] = i
        return
        