# group anagrams
# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in strs:
            # s_i = ''.join(sorted(i)) # this can be improved, it takes n log(n) to sort
            s_i = [0]*26
            for s in i:
                s_i[ord(s) - 97] += 1
            s_i = str(s_i)
            if s_i not in map:
                map[s_i] = [i]
            else:
                map[s_i].append(i)

        return  map.values()