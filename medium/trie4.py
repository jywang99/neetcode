class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.children.keys():
                n.children[c] = TrieNode()
            n = n.children[c]
        n.end = True

    def __getNode(self, word) -> TrieNode|None:
        n = self.root
        for c in word:
            n = n.children.get(c)
            if not n:
                return None
        return n

    def search(self, word: str) -> bool:
        n = self.__getNode(word)
        return n is not None and n.end

    def startsWith(self, prefix: str) -> bool:
        return self.__getNode(prefix) is not None
        
