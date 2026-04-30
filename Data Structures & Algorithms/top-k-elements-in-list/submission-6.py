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
        #bucket sort
        bucket = [[] for _ in range(len(nums))]
        for key, value in freq_dict.items():
            bucket[value-1].append(key)
        for ndx in range(len(nums), 0, -1):
            if len(ret) == k:
                return ret
            ret.extend(bucket[ndx-1])
        return ret[:k]