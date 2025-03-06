from typing import Optional


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
            if c not in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]
        n.end = True

    def __getLastNode(self, word: str) -> Optional[TrieNode]:
        n = self.root
        for c in word:
            n = n.children.get(c)
            if not n:
                return None
        return n

    def search(self, word: str) -> bool:
        n = self.__getLastNode(word)
        return (n is not None) and n.end

    def startsWith(self, prefix: str) -> bool:
        return self.__getLastNode(prefix) is not None

