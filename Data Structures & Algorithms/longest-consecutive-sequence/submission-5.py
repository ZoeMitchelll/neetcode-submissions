class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        ret = 0
        for num in all_nums: #[0]
            curr = num
            longest = 0
            if num - 1 not in all_nums:
                print(num, curr, curr in all_nums)
                while curr in all_nums:
                    curr = curr + 1
                    longest = longest + 1
                if longest > ret:
                    ret = longest
        return ret
            
            