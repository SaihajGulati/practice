class Solution:
    #T: O(nm) M: O(min(m, n)) if use if statement otherwise O(m)
  
        #is like running recursion, bc that's what dp is
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False


        #IF WANTED TO, COULD ADD THIS GENIUS
        #dp row is length of s2, so let's make sure s2 is smaller one by switching if isn't
        #slight tradeoff of time vs memory bc swap requires traversing through one of the string's contents which adds a bit of time
        #but time tradeoff does not materially change time complexity while this does meaningfully reduce memory complexity
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        dpRow = [False] * (len(s2) + 1)
        dpRow[-1] = True #bc at start this is the part that is off the lens for both

        #handles bottom row so that can do in one row in loop below and don't have to weird if condition
        for j in reversed(range(len(s2))):
            #since is bottom row, len(s1) instead of i
            if s2[j] == s3[len(s1) + j] and dpRow[j + 1]:
                    dpRow[j] = True

        for i in reversed(range(len(s1))):
            newRow = [False] * (len(s2) + 1)
            #have to put last one of newRow to what would be if loop went all the way
            #to avoid weird if condition
            newRow[-1] = s1[i] == s3[i + len(s2)] and dpRow[len(s2)]

            for j in reversed(range(len(s2))):
                #if equal to index we're at in s3, and one below is true (the one right after the letter we're at in s1), let's use it and mark this as true bc it works
                if s1[i] == s3[i + j] and dpRow[j]:
                    newRow[j] = True
                #if equal to index we're at in s3, and one to right is true (so using the one after this in s2), let's use it and mark this as true bc it works
                #made this elif only bc this version of code will be faster with elif
                #but in recursive version gotta check both bc is each case
                elif s2[j] == s3[i + j] and newRow[j + 1]:
                    newRow[j] = True
            dpRow = newRow
        return dpRow[0]
