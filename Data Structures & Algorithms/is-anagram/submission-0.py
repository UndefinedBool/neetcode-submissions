class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        g = len(s)
        if g != len(t):
            return False
        s2 = ''.join(sorted(s))
        t2 = ''.join(sorted(t))
        for i in range(g):
            if s2[i] != t2[i]:
                return False
        return True

        
            

            