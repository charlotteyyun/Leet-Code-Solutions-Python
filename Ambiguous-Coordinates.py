"""
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
Example 2:
Input: "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation:
0.0, 00, 0001 or 00.01 are not allowed.
Example 3:
Input: "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
Example 4:
Input: "(100)"
Output: [(10, 0)]
Explanation:
1.0 is not allowed.


Note:

4 <= S.length <= 12.
S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.
"""
def sc2std(x):
    s = str(x)
    if 'e' in s:
        num,ex = s.split('e')
        if '-' in num:
            negprefix = '-'
        else:
            negprefix = ''
        num = num.replace('-','')
        if '.' in num:
            dotlocation = num.index('.')
        else:
            dotlocation = len(num)
        newdotlocation = dotlocation + int(ex)
        num = num.replace('.','')
        if (newdotlocation < 1):
            return negprefix+'0.'+'0'*(-newdotlocation)+num
        if (newdotlocation > len(num)):
            return negprefix+ num + '0'*(newdotlocation - len(num))+'.0'
        return negprefix + num[:newdotlocation] + '.' + num[newdotlocation:]
    else:
        return s
class Solution:
    def ambiguousCoordinates(self, S):
        if S == "()":
            return []

        globallist = []
        for i in range(2, len(S) - 1):
            s1 = S[1:i]
            s2 = S[i:len(S) - 1]
            f1 = []
            f2 = []
            first = int(s1)
            second = int(s2)
            if str(first) == s1 and str(second) == s2:
                globallist.append(S[:i] + ", " + S[i:])
            for j in range(1, len(s1)):
                sf = s1[:j] + '.' + s1[j:]
                f = float(sf)
                if (str(f) == sf or sc2std(f) == sf) and int(f) != f:
                    f1.append(sf)
            for k in range(1, len(s2)):
                sf = s2[:k] + '.' + s2[k:]
                f = float(sf)
                if (str(f) == sf or sc2std(f) == sf) and int(f) != f:
                    f2.append(sf)
            for elem in f1:
                if str(second) == s2:
                    globallist.append("(" + elem + ", " + s2 + ")")
                for e in f2:
                    globallist.append("(" + elem + ", " + e + ")")
            for k in f2:
                if str(first) == s1:
                    globallist.append("(" + s1 + ", " + k + ")")

        return (globallist)