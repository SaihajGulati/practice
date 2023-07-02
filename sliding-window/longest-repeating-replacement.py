class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        maxLetter = ""
        maxCount = 0
        maxLen = 0

        #r is right index, c is char in string
        for r, c in enumerate(s):         
            #increase count of r
            count[c] += 1
            
            """if wasn't defaultdict, could do this:
            count[c] = 1 + count.get(c, 0)
            """
            
            #don't need maxLetter because if you notice, each time we use just the maxCount
            maxCount = max(maxCount, count[c])
            
            #since start with 0 changes, need this check after above
            #check k
            #no while needed in this version bc will only run once either way as maxcount isn't changing
            #so all we're doing is moving left one up
            #would work with while loop too but regardless runs literally once if use the method where maxCount is not changed here
            if (r - l + 1 - maxCount) > k:
            """if used array or hashmap of size 26 to track count:
            while (r - l + 1 - max(count.values())) > k:
            ***don't need though because can overcompensate and check correctly by just checking maxCount ever seen
            """"
                #need to reduce count first so do it for correct l
                #works even though don't reset maxCount because maxCount of all maxCounts is going to be in the longest string we can do with k
                #bc, think, if get longer substring length than maxLen, would need maxCount to be bigger than old maxCount too, 
                #otherwise will be greater than k difference since k is constant
                count[s[l]] -= 1
                l += 1

            #check/set max every time
            #downw here because needs to be after adjust length above with check of whether this r-l and maxCount works
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
