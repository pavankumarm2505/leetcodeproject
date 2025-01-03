class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # Anagrams must have the same length
            return False
        liss = {}
        for i in s:
            liss[i] = liss.get(i,0)+1
        for i in t:
            if i not in liss or liss[i]==0:
                return False
            liss[i] -=1

        return True