class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq dict (O(n) space and O(n) time)
        # create a bst which should automatically return false for a duplicate (O(n) space O(n) time)
        # sort the list and then keep track of the last seen num and make sure you haven't seen that one (O(n) space O(nlogn) time)
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False