class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn to set for every number in nums check how many consecutive are in the set
        # for every num create tuple of start and end and list of len(nums) size and fill those lists check for consecutive at end
        all_nums = set(nums)
        ret = 0
        for num in nums: #[0]
            curr = num
            longest = 0
            # i want to make sure -1 is not in all_nums (smallest)
            # print(num, curr, num -1 in all nums, num )
            if num - 1 in all_nums:
                pass
            else:
                print(num, curr, curr in all_nums)
                while curr in all_nums:
                    curr = curr + 1
                    longest = longest + 1
                if longest > ret:
                    ret = longest
        return ret
            
            