class Solution(object):
    """
    - story (of problem in terms of what should do): checck is string is palindrome
    - input: string
    - output: boolean
    - Requirements: return true if is palindrome, false otherwise
    - base cases/edge cases: when odd number, have to check until middle values (length/2 index or length-1 over 2) and when even have to check until second to omiddle value on each side (length-1 over 2 index)
    - Constraints that could help:
    - Algo (thinking of): Two pointer, one from each end but have to get ride of alphanumeric and have to convert each time
    So when would end? would end when left passes right
    """
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while left <= right:
            #first check if each thing is valid, python helps but could use own function or check using ord which is ascii
            if (not s[left].isalnum()):
                left += 1
            elif (not s[right].isalnum()):
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
              #important to make it through the else because this will force re-check at top of left <= right which is needed
            else:
                left += 1
                right -= 1

        return True
