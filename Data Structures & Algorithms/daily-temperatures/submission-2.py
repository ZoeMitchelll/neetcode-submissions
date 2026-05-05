class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #n^2 nestled loops
        #can I iterate through, and make a min stack?
        minstack = []
        otherstack = []
        ret = [0 for x in range(len(temperatures))]
        for ndx in range(len(temperatures)-1,-1,-1): #[30,30,38] [2,1,0]
            days = 0
            while minstack:
                days += 1
                last_temp = minstack.pop() #30
                otherstack.append(last_temp)
                if last_temp > temperatures[ndx]:
                    ret[ndx] = days
                    break
            minstack.extend(otherstack[::-1]) #put everything back
            otherstack = []
            minstack.append(temperatures[ndx]) #add today before looking at yesterfay
        return ret
            