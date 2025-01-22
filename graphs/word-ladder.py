class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        words, result = set(wordList), 0
        q = deque([beginWord])
        while q:
            result += 1
            for _ in range(len(q)): #does all at this level, so are counting number of layers or times did
                node = q.popleft()
                if node == endWord:
                    return result
                for i in range(len(node)): #try to see one letter changed for each, is much faster than looking at all words if one off
                    for c in range(97, 123):
                        if chr(c) != node[i]:
                            nextWord = node[:i] + chr(c) + node[i + 1:]
                            if nextWord in words:
                                q.append(nextWord)
                                words.remove(nextWord)
        return 0
