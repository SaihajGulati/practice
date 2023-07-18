class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        #T: O(n^2) bc check up to entire string (n) for each middle letter (n times)
        #M: O(1)
        #Approach: try each one as a middle of the palindrome
        #better than checking start of palindrome bc checking that is horrific timewise bc have to do length of string for each check while this builds up so each check is just an if statement
        #requires checking if is even size and odd size
        for i in range(len(s)):
            #
            # odd length check(so go outward from middle one)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    #clean way to get substring
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length (so go outward from middle two)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
