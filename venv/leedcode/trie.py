



class Trie:

    def __init__(self):
        self.root = {}
        self.endWord = "#"


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.endWord] = self.endWord

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.endWord in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def run() :
    obj = Trie()
    obj.insert("apple")
    p2 = obj.search("app")
    p3 = obj.startsWith("app")
    print("p2 = ", p2)
    print("p3 = ", p3)