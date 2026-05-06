class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #O(p*t) list of lists where i find the position until target for each car and then iterate through them and make the fleets (brute)
        #make position/speed dictionary and hen if keys clash i'll return the dictionary size
        #i know this is a stack problem somehow???
        #hard stop at target
        #cars cannot pass so fleet = len(position) -1 if a car's position is no longer sorted its a pass
        #
        position = sorted(enumerate(position), key=lambda x: x[1], reverse=True)
        fleets = len(position)
        for ndx in range(len(position)):
            travel_time = (target-position[ndx][1])/speed[position[ndx][0]]
            position[ndx] = travel_time
        print(position)
        for ndx in range(len(position)-1):
            if position[ndx] >= position[ndx+1]:
                fleets = fleets -1
                position[ndx+1] = position[ndx]
        return fleets