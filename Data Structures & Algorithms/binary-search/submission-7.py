class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            ndx = (high+low)//2
            if nums[ndx] == target:
                return ndx
            elif nums[ndx] < target:
                low = ndx + 1
            else:
                high = ndx - 1
        return -1