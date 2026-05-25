class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else:
            s = s.lower()
            t = list(t.lower())
            check = 0
            for i in range (len(s)):
                if s[i] in t:
                    t.remove(s[i])
                
            if t:
                return False
            else:
                return True
