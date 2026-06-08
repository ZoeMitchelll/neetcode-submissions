class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        
        for i in range(len(nums)):
            # Skip the same starting number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            pair_sum = -nums[i]
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                current_sum = nums[j] + nums[k]
                
                if current_sum < pair_sum:
                    j += 1
                elif current_sum > pair_sum:
                    k -= 1
                else:
                    # Found a triplet
                    ret.append([nums[i], nums[j], nums[k]])
                    
                    # Move both pointers and skip duplicate values
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ret