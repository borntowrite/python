# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.leaves:
                curr.leaves[c] = TrieNode()
            curr = curr.leaves[c]
        curr.is_string = True

    def search(self, word):
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, start, curr):
        if start == len(word):
            return curr.is_string
        if word[start] in curr.leaves:
            print("dict :", curr.leaves)
            return self.searchHelper(word, start+1, curr.leaves[word[start]])
        # elif word[start] == '.':
        #     for c in curr.leaves:
        #         if self.searchHelper(word, start+1, curr.leaves[c]):
        #             return True

        return False

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.addWord("pattern")
wordDictionary.addWord("past")
print(wordDictionary.search("word"))
