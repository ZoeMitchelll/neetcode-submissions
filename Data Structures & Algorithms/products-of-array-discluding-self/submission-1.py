class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #find product, divide by num brute force not allowed
        #for nums multiply 
        ret = [1]*len(nums)
        for ndx in range(len(ret)):
            if ndx > 0:
                ret[ndx] = ret[ndx-1] * nums[ndx-1]
        prod = 1
        for ndx in range(len(ret)-1, -1, -1):
            ret[ndx] = ret[ndx] * prod
            prod = prod * nums[ndx]
        return ret
        