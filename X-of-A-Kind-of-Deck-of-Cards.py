"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000
 
"""

class Solution(object):
    def hasGroupsSizeX(self, deck):
        # if len(deck) <= 1: return false
        if len(deck) <= 1:
            return False

        # get d = a list of unique cards in deck
        d = list(set(deck))
        # get c = the deck.count of each unique card
        c = [deck.count(n) for n in d]
        # if list(set(c)) == 1: return true
        if list(set(c)) == 1:
            return True
        # return all(i%min(list(set(c))) == 0 for i in list(set(c)))
        u = list(set(c))
        m = min(u)
        return all(math.gcd(i, m) != 1 for i in u)

        """
        :type deck: List[int]
        :rtype: bool
        """