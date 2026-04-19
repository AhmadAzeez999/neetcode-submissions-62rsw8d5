class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [index, height]
        largestRect = 0

        for i in range(len(heights)):
            index = i
            while stack and (stack[-1][1] > heights[i]):
                stackI, stackH = stack[-1][0], stack[-1][1]
                area = stackH * (i - stackI)
                largestRect = max(largestRect, area)
                index = stackI
                stack.pop()
            stack.append([index, heights[i]])

        while stack:
            stackI, stackH = stack[-1][0], stack[-1][1]
            area = stackH * (len(heights) - stackI)
            largestRect = max(largestRect, area)
            stack.pop()

        return largestRect