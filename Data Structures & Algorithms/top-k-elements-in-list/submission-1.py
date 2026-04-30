from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create freq dictionary and then iterate adding to list (n space and n time)
        #sort then counter var that resets with every unique num and if counter >=k add to ret (nlogn time, m space) m is num in ret value
        #
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] +=1
        ret = []
        for key, value in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True):
            ret.append(key)
        return ret[:k]