class Node:
    def __init__(self, isWord = False):
        self.isWord = False
        ##hashmap use always over 26 list unless they make u bc of cracked searching code in python
        ##will have node object in it if letter is next
        #don't even need char because is stored in hashmap and/or this childnren list, but could have if wanted
        self.children = {}

        #don't worry about getter/setter because in most languages will be a struct for node, which means everything is default publicc

class WordDictionary:
    #memory is much worse with recursion all the way because have to add to stack
    #hence, other solution is better because minimizes recursion while still being easily codable
    def __init__(self):
        #smart to do so here so don't have to worry below
        #need root like this instead of head pointer because:
        #allow for true root always being maintained because otherwise you never know the true root of the tree because it couold be rewritten anytime a word with a different first letter is added
        self.root = Node()
    
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            #checks if c is a key
            if c not in curr.children:
                curr.children[i] = Node()
            
            #this will set curr to the next node
            #have to do regardless of whether just added or already exists
            curr = curr.children[i]

        #at end of loop, need to set the node to being the end of a word
        #is already stored as curr so bet
        curr.isWord = True  

    def search(self, word):
        #in another language, would have to be nonnested so would need to pass word string too
        #better to pass index than doing with just word and curr passed, because then have to pass sliced substring each time
        #which passes a copy and has memory overhead
        def searchHelper(index, curr):
            #curr at the end will be the last child/letter used
            if index == len(word):
                return curr.isWord

            for i in range(index, len(word)):
              c = word[i]
              if c == ".":
                  #this will go through only the values so all the noes that exist
                  #also why hashmap is better bc won't chekc all 26 to figure out which exist and which don't and avoid some non checking stuff
                  for child in curr.children.values():
                      if searchHelper(i + 1, child):
                          return True
                  #if make it here, didn't find a letter that's a child and valid for this word
                  return False
              #is just a letter so do more normal task
              else:
                  #first check if there is even a child node for this letter
                  if c not in curr.children:
                      return False
                  #is a letter seen and need to move on
                  curr = curr.children[c]
            
              #if get to end of for loop, need to check if the last indicator shows this is a word
              return curr.isWord

        return searchHelper(0, self.root)
            




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
