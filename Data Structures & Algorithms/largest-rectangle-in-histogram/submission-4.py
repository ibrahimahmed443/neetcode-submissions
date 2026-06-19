class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []      # (start_index, height) pair
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                area = h * (index - idx)
                maxArea = max(maxArea, area)
                start = idx     # extend the current index backwards as this height is smaller

            stack.append((start, height))

        # some heights may be extended all the way to the end, so calculate max height for them
        n = len(heights)
        for idx, h in stack:
            area = h * (n - idx)
            maxArea = max(maxArea, area)

        return maxArea
