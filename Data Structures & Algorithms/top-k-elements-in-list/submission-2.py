class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        real = []
        
        letters = {}
        
        for i in range(len(nums)):
            if nums[i] in letters:
                letters[nums[i]] += 1
            else:
                letters[nums[i]] = 1
        combined = list(zip(letters.values(), letters.keys()))
        combined.sort()
        combined = combined[::-1]
        
        for i in range(k):
            real.append(combined[i][1])
        return real