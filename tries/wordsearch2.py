#has better memory than neet's way
#my way doesn't remove the word from the trie, his final solution does
#his way ends up slightly faster, but way more work happening in memory

class TrieNode:
    def __init__(self, isWord = False):
        self.isWord = isWord
        self.children = {}
    #from neet's final solution, he calls root.removeWord in the if statement that adds to result
    #and of course call root.addWord where I do the work in the first for loop
    # def addWord(self, word):
    #     cur = self
    #     cur.refs += 1
    #     for c in word:
    #         if c not in cur.children:
    #             cur.children[c] = TrieNode()
    #         cur = cur.children[c]
    #         cur.refs += 1
    #     cur.isWord = True

    # def removeWord(self, word):
    #     cur = self
    #     cur.refs -= 1
    #     for c in word:
    #         if c in cur.children:
    #             cur = cur.children[c]
    #             cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #first need to add all to prefix tree
        root = TrieNode() #dummy node
        for word in words:
            #start at root while filling prefix tree
            curr = root
            for c in word:
                if c not in curr.children:
                    #need to add new child if not there right now
                    newNode = TrieNode()
                    curr.children[c] = newNode
                curr = curr.children[c] #have to jump to it either ways
            #once get here, word is done, so mark as a word
            curr.isWord = True

        rows = len(board)
        cols = len(board[0])
        visited = [[0] * cols for i in range(rows)] #visited can be a set of tuples too, not much difference either way
        word = ""
        result = set()

        #now run dfs using prefix tree as a guide
        def dfs(i, j, curr):
            nonlocal word
            if (
                i >= rows or
                j >= cols or
                i < 0 or
                j < 0 or
                visited[i][j] or
                board[i][j] not in curr.children
                ):
                return
            
            visited[i][j] = 1
            word += board[i][j]
            curr = curr.children[board[i][j]]

            if curr.isWord:
                result.add(word)
                curr.isWord = False #key way to make slightly faster, as will not add duplicates then
                #this line actually makes it useless to have the result be a set; with it being a list you are ensured no duplicates
                #doesn't affect time much because is just one pass through result list but still technically faster to just have it be a list then

            dfs(i + 1, j, curr)
            dfs(i - 1, j, curr)
            dfs(i, j - 1, curr)
            dfs(i, j + 1, curr)

            #undo since backtracking
            visited[i][j] = 0
            word = word[:-1]

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        
        return list(result)
