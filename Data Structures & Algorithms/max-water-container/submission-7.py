class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0
        while l<r:
            height = min(heights[l], heights[r])
            width = r - l
            max_water = max(max_water, width*height)
            if heights[l] < heights[r]:
                l+=1
            else:
                r = r - 1
        return max_water