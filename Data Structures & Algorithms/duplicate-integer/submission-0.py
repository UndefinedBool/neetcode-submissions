class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = []
        for i in nums:
            if i in prev:
                return True
            else:
                prev.append(i)
        return False
        