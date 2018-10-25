"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
class Solution(object):
    def reorganizeString(self, S):
        l = set([i for i in S])
        c = [S.count(i) for i in l]
        if max(c) - (len(S) - max(c)) > 1:
            return ""
        p = sorted([(x,y) for x,y in zip(c,l)])
        A = []
        for x,y in p:
            A.extend(x*y)
        ans = [None] * len(S)
        ans[::2], ans[1::2] = A[len(S)/2:], A[:len(S)/2]

        return ''.join(ans)
        """
        :type S: str
        :rtype: str
        """