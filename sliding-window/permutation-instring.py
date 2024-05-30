# T: O(n)
# M: O(1) because two lists of size 26 max
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #immediate fail
        if len(s1) > len(s2):
            return False

        #setup both lists, having checked first few letters of s2 that line up with length of s1
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            #notice use of ord to get index
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        #calculate matches --> O(26) operation
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        #go through each window
        l = 0
        for r in range(len(s1), len(s2)):
            #anytime get 26 matches, have found the permutation that's in the string
            if matches == 26:
                return True

            #handling r movement part (seeing a new letter)
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            #might've added a match
            if s1Count[index] == s2Count[index]:
                matches += 1
            #s2count is one more than s1count, means was a match with s1 before the one was added to s2's count
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            #handling l movement part (removing a letter seen already)
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            #now matches after the removal
            if s1Count[index] == s2Count[index]:
                matches += 1
            #s2count is one less than s1count, means was a match with s1 before the one was removed from s2's count
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        
        #have to do at end in case the last one gives the permutation, since don't get to check at start of next iteration loop here
        return matches == 26 
