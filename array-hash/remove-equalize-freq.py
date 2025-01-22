class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(word) == 2:
            return True
        freq = {}
        for c in word:
            freq[c] = freq.get(c, 0) + 1

        keysList = freq.keys()
        sortedKeys = sorted(keysList, key = lambda x : freq[x])

        if len(sortedKeys) == 1: #means all same letter
            return True

        setFreq = freq[sortedKeys[0]]

        if setFreq == 1:
            #first part means if all have frequency of 1, then can remove so good
            #second part is saying if the second frequency is the same as the last one, means only the first one is different (and is 1), so can remove that and are good
            if freq[sortedKeys[-1]] == setFreq or freq[sortedKeys[1]] == freq[sortedKeys[-1]]:
                return True
        
        #need to check all just in case where have multiple freq that are one more than first (and not enough to have all but one which would satisfy above)
        #this is because that case would show up as true in the return statement condition but shouldn't
        for i in range(len(sortedKeys) - 1):
            if freq[sortedKeys[i]] != setFreq:
                return False
       
        return freq[sortedKeys[-1]] == setFreq + 1



        
