class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #find product, divide by num brute force not allowed
        #for nums multiply 
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        for ndx in range(len(prefix)):
            if ndx > 0:
                prefix[ndx] = prefix[ndx-1] * nums[ndx-1]
        for ndx in range(len(suffix), 0, -1):
            if ndx < len(suffix):
                suffix[ndx-1] = suffix[ndx] * nums[ndx]
        print(prefix)
        print(suffix)
        return [prefix[ndx]*suffix[ndx] for ndx in range(len(nums))]
        