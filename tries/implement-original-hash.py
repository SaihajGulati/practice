class Node(object):
    def __init__(self, char = "", word = False):
      #can simplify this a lot by not having char or word in constructor as word is always false
      #and don't need to track char as is done by spot in map or spot in letter array
        self.char = char
        self.word = word
        self.next = {}

class Trie(object):

    def __init__(self):
        self.dummy = None
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if not self.dummy:
            self.dummy = Node()

            """for num in range (1, len(word)):
                #is a node for the new letter
                newNode = Node(word[num])
                
                #add a dictionary entry for this letter and new node
                curr.next[word[num]] = newNode
                curr = newNode

            curr.word = True
        else:"""
        curr = self.dummy
        for c in word:
            #check if letter already in and then move on
            """
            you can make this all into one if statement with only one resetting of curr outside of if,
            by checking for if not c in curr.next
            """
            if c in curr.next:
                curr = curr.next[c]
            else:
                newNode = Node(c)
                #add a dictionary entry for this letter and new node
                curr.next[c] = newNode
                curr = newNode
        curr.word = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not self.dummy: 
            return False
        
        curr = self.dummy
        
        for c in word:
            #check if letter already in and then move on
            if not (c in curr.next):
                return False
            #else c is in curr.next keys so move to that node
            curr = curr.next[c]
        #once get here, curr is the last letter of the word but only return true if is a terminal node
        return curr.word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if not self.dummy: 
            return False
        
        curr = self.dummy
        
        for c in prefix:
            #check if letter already in and then move on
            if not (c in curr.next):
                return False
            #else c is in curr.next keys so move to that node
            curr = curr.next[c]
        #once get here, this time don't need to check if terminal so just return True
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
