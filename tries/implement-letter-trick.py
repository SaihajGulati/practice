class Node(object):
    def __init__(self, word = False):
        self.word = word
        #uses fact that letters can only be 26 different as is only lowercase as way to avoid using dictionary
        self.next = [None]*26

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

        curr = self.dummy

        for c in word:
            index = ord(c) - ord('a')
            #if none, means does not already exist
            if not curr.next[index]:
                #add a dictionary entry for this letter and new node
                curr.next[index] = Node()
            curr = curr.next[index]
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
            index = ord(c) - ord('a')
            #check if not in next, which means don't have word
            if not curr.next[index]:
                return False
            #else c is in curr.next keys so move to that node
            curr = curr.next[index]
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
            index = ord(c) - ord('a')
            #check if not in next, which means don't have word
            if not curr.next[index]:
                return False
            #else c is in curr.next keys so move to that node
            curr = curr.next[index]
        ##once get here, this time don't need to check if terminal so just return True
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
