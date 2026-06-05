class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frq = counter.most_common(k)
        ans = []

        for x, y in frq:
            ans.append(x)
        
        return ans
        