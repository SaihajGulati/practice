class Solution:
    # T: O(n^2) bc max x times for each letter in string (n * n)
    # M: O(1)

    #really similar to longest palindromic substrings, just with finding pals for each letter made into a function so less repeated code
    def countSubstrings(self, s: str) -> int:
        def countPals(l, r, s):
            res = 0
            #while in range and equal (so is a palindrome then)
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
            return res
        
        res = 0
        for i in range(len(s)):
            #find all pals with odd length so one letter in middle
            res += countPals(i, i, s)

            #find all pals with even length so two letters in middle that are same
            res += countPals(i, i + 1, s)
        
        return res
