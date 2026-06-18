class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        maxArea = 0
        for i in range(0, len(heights)):
            minimum = heights[i]
            for j in range(i, len(heights)):
                minimum = min(minimum, heights[j])
                area = minimum * (j - i + 1)
                maxArea = max(maxArea, area)
        
        return maxArea