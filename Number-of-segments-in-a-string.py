"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

class Solution(object):
    def countSegments(self, s):
        list_words = s.split()
        return (len(list_words))
        """
        :type s: str
        :rtype: int
        """
