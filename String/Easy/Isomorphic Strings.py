
##LeetCode 205. Isomorphic Strings
##TC: O(n)
##SC: O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashmap1 = {}
        hashmap2 = {}

        s1 = []
        s2 = []

        for i in range(len(s)):
            if s[i] not in hashmap1:
                hashmap1[s[i]] = i
            s1.append(hashmap1[s[i]])

            if t[i] not in hashmap2:
                hashmap2[t[i]] = i
            s2.append(hashmap2[t[i]])

        if s1 == s2:
            return True
        return False