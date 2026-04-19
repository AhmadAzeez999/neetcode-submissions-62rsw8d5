class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [index, height]
        largestRect = 0

        for i, h in enumerate(heights):
            start = i
            while stack and (stack[-1][1] > h):
                stackI, stackH = stack[-1][0], stack[-1][1]
                largestRect = max(largestRect, stackH * (i - stackI))
                start = stackI
                stack.pop()
            stack.append([start, h])

        while stack:
            stackI, stackH = stack[-1][0], stack[-1][1]
            largestRect = max(largestRect, stackH * (len(heights) - stackI))
            stack.pop()

        return largestRect