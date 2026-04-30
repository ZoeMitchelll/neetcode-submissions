class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force n^2 time 1 space itertools.product
        #check if sorted/sort and then do two pointers (move one down if the sum is too big and move one up if its too small) nlogn+n time and n spcae (new list)
        #target - index in a dictionary and if the key is in the ictionary return both (n time and n space)
        num_ndx = dict()
        for ndx in range(len(nums)):
            if nums[ndx] in num_ndx: #nums[1] = 4
                return [num_ndx[nums[ndx]], ndx]
            num_ndx[target-nums[ndx]] = ndx #num_ndx[7-3] = 0
        