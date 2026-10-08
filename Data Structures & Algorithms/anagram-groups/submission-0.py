class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicty = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            dicty[sortedS].append(s)
        return list(dicty.values())