class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHashMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            countHashMap[num] = countHashMap.get(num, 0) + 1
        for num, count in countHashMap.items():
            freq[count].append(num)
        res = []
        for x in range(len(freq) - 1, 0, -1):
            for y in range(len(freq[x])):
                res.append(freq[x][y])
                if len(res) == k:
                    return res
        return res