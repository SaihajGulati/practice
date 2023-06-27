class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #default dict is like dictionary but when empty thing is accessed/modified, gives a default value instead of keyError
        anagrams = defaultdict(list)
        
        #go through all words in list given
        for word in strs:
            letterCount = [0] * 26
            #fill in count array
            for c in word:
                letterCount[ord(c)-ord('a')] += 1
            
            #can't hash list, but can with tuple so have to convert
            #since using defaultdict above, don't have to use get to check if exists
            anagrams[tuple(letterCount)].append(word)
            
          #if anagrams was a normal dictioary, would need to check with get like this:
            """
            if anagrams.get(tuple(letterCount)):
                anagrams[tuple(letterCount)].append(word)
            else:
                anagrams[tuple(letterCount)] = [word]
            """

        #need to wrap in list because values returns a view object not a list
        return anagrams.values()
