class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = list(s)
        t_arr = list(t)

        return sorted(s_arr) == sorted(t_arr)
        