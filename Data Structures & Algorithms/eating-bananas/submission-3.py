class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1
        while min_k < max_k:
            this_k = (max_k+min_k)//2
            this_time = self.checkK(piles, this_k)
            if this_time > h:
                min_k = this_k+1
            else:
                max_k = this_k
        return min_k

    def checkK(self, piles: List[int], h: int) -> int:
        time = 0
        for banana in piles:
            time += -(-banana//h)
        return time
        