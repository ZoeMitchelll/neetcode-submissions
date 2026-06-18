class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: #[3,6,7,11] 8
        max_k = max(piles)
        min_k = 1
        #check in the middle to see if the time is
        #if time is greater than h then the number moves up
        #if the number is less than h than it goes down
            #if the number is greater than h again then return
        while min_k < max_k:
            this_k = (max_k+min_k)//2 #3
            this_time = self.checkK(piles, this_k) #10
            print(max_k, min_k, this_k, this_time)
            if this_time > h:
                min_k = this_k+1 #2
            else:
                max_k = this_k
            print(min_k, max_k)
        return min_k

    def checkK(self, piles: List[int], h: int) -> int:
        time = 0
        for banana in piles:
            time += -(-banana//h)
        return time
        