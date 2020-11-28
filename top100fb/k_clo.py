# K closest
# url: https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List


class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
