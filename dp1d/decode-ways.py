#T: O(n)
#M: O(1) because of smart strat of using two variables instea of list for 1d dp
class Solution:
    def numDecodings(self, s: str) -> int:
        #only values we need for dp, so can avoid list[i]
        #two = dp[i+1], one = dp[i+2], temp = dp[i]
        two = 1
        one = 1
        for i in reversed(range(len(s))):
            if s[i] == "0":
                temp = 0
            else:
                temp = one
            #last part is easy way to check if string is between inclusive 0 and 6 as needed
            if i < len(s)-1 and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                temp += two
            two = one
            one = temp
        return one
