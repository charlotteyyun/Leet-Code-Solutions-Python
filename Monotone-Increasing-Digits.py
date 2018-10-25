"""
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        if N < 10:
            return N
        l = [int(i) for i in str(N)]
        if all(l[i] >= l[i - 1] for i in range(1, len(l))):
            return N
        backup = 0
        for n in range(1, len(l)):
            if l[n] == l[n - 1]:
                backup += 1
            elif l[n] > l[n - 1]:
                backup = 0
            elif l[n] < l[n - 1]:
                n -= backup
                l[n - 1] -= 1
                l = l[:n] + [9] * (len(l) - n)
                break

        return int("".join(map(str, l)))
        """
        :type N: int
        :rtype: int
        """
