class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0):
            return 0

        left = 0
        right  = 1
        currLetters = set()
        currLetters.add(s[left])
        maxLength = 1
        
        ##could do for loop here for right and then below if needs to be why, but this is more intuitive for me 
        ##(evens out ish because this requires more checking of right against length and that checks more if right is in currLetters) 
        while right < len(s):
            ##get a duplicate letter, change window
            if (s[right] in currLetters):
                ##really important here to remove the left value and NOT the duplicate one because this way you're acctually changing the window
                currLetters.remove(s[left])
                left += 1
            ## is new letter, so add to curr String and compare
            else: 
                currLetters.add(s[right])
                maxLength = max(len(currLetters), maxLength)
                right += 1
        return maxLength
