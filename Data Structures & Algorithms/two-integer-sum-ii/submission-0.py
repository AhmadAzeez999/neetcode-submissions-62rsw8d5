class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lPtr, rPtr = 0, len(numbers) - 1
        while lPtr < rPtr:
            currentSum = numbers[lPtr] + numbers[rPtr]
            if currentSum == target:
                return [lPtr+1, rPtr+1]
            elif currentSum < target:
                lPtr += 1
            elif currentSum > target:
                rPtr -= 1
        return