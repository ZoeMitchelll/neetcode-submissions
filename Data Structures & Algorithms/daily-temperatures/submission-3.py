class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #n^2 nestled loops
        #can I iterate through, and make a min stack?
        monotonicstack = []
        ret = [0 for x in range(len(temperatures))]
        for ndx in range(len(temperatures)): #[30,30,38] [2,1,0]
            print(ndx, monotonicstack, temperatures[ndx], temperatures[ndx-1])
            while monotonicstack and temperatures[ndx] > temperatures[monotonicstack[-1]]:
                prev_i = monotonicstack.pop()
                ret[prev_i] = ndx - prev_i
            print(ndx, monotonicstack, ret)
            monotonicstack.append(ndx) #add today before looking at yesterfay
        return ret
            