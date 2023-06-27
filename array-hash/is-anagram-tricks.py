class Solution(object):
    """
    - story (of problem in terms of what should do): check if anagrams of each other
    - input: two strings
    - output: boolean
    - Requirements: return true if anagrams, false if not
    - Constraints that could help:
    - base cases: if different length then not same
    - Algo (thinking of): use hashSets --> 
    - what is an anagram --> same leters and same amount of all letters
    - maybe make a dictionary and then see is same
    - worse memory than original
    """
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dictS, dictT = {}, {}
        #goes through s and then if the letter is in dict, then adds 1 to count, otherwise, adds 1 to new entry starting with vaue 0
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)

        return dictT == dictS #returns true is anagrams and false otherwise
