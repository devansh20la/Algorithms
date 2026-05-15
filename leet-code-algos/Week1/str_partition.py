# str_partition
# https://leetcode.com/problems/partition-labels
from typing import List


# Brute force
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ends = {s: i for i, s in enumerate(S)}
        curr = 0
        out = [0]

        while (curr < len(S)):
            last = ends[S[curr]]
            while curr < last:
                s = S[curr]
                last = max(last, ends[s])
                curr +=1
            out.append(curr)
        return [out[i] - out[i - 1] for i in range(1, len(out))]


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ends = {s: i for i, s in enumerate(S)}
        j = 0
        ans = []
        for i, s in enumerate(S):
            j = max(j, ends[s])

            if i == j:
                if len(ans) > 0:
                    ans.append(i + 1 - sum(ans))
                else:
                    ans.append(i+1)
        return ans


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))