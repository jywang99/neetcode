from typing import cast


class TrieNode:
    def __init__(self):
        self.children: list[TrieNode|None] = [None]*26
        self.tail = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = self.root
        for c in word:
            i = ord(c) - ord("a")
            if not n.children[i]:
                n.children[i] = TrieNode()
            n = cast(TrieNode, n.children[i])
        n.tail = True

    def search(self, word: str) -> bool:
        n = self.root
        for c in word:
            n = n.children[ord(c) - ord("a")]
            if not n:
                return False
        return n.tail

    def startsWith(self, prefix: str) -> bool:
        n = self.root
        for c in prefix:
            n = n.children[ord(c) - ord("a")]
            if not n:
                return False
        return True

