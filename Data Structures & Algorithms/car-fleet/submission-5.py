class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #O(p*t) list of lists where i find the position until target for each car and then iterate through them and make the fleets (brute)
        #make position/speed dictionary and hen if keys clash i'll return the dictionary size
        #i know this is a stack problem somehow???
        #hard stop at target
        #cars cannot pass so fleet = len(position) -1 if a car's position is no longer sorted its a pass
        #stack problem because its sorted by decending
        position = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleets = []
        for p, s in position:
            travel_time = (target-p)/s
            if fleets:
                leading_time = fleets[-1]
                if leading_time < travel_time:
                    fleets.append(travel_time)
            else:
                fleets.append(travel_time)
        return len(fleets)