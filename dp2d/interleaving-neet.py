class Solution:
    #T: O(nm) M: O(nm)
    #is like running recursion, bc that's what dp is
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                #if equal to index we're at in s3, and one below is true (the one right after the letter we're at in s1), let's use it and mark this as true bc it works
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                #if equal to index we're at in s3, and one to right is true (so using the one after this in s2), let's use it and mark this as true bc it works
                #made this elif only bc this version of code will be faster with elif
                #but in recursive version gotta check both bc is each case
                elif j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
