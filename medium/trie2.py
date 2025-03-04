from typing import cast


class TrieNode:
    def __init__(self) -> None:
        self.children: list[TrieNode|None] = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not n.children[i]:
                n.children[i] = TrieNode()
            n = cast(TrieNode, n.children[i])
        n.end = True

    def __getLastNode(self, word: str) -> TrieNode|None:
        n = self.root
        for c in word:
            n = n.children[ord(c) - ord('a')]
            if not n:
                return None
        return n

    def search(self, word: str) -> bool:
        n = self.__getLastNode(word)
        if not n:
            return False
        return n.end

    def startsWith(self, prefix: str) -> bool:
        return self.__getLastNode(prefix) != None

