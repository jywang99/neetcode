from typing import Optional, cast


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


class WordNode:
    def __init__(self) -> None:
        self.children: dict[str, WordNode] = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                n = WordNode()
                cur.children[c] = n
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def recurse(cur: Optional[WordNode], i: int) -> bool:
            if not cur:
                return False

            if i == len(word):
                return cur.end

            c = word[i]
            if c == ".":
                for n in cur.children.values():
                    if recurse(n, i+1):
                        return True
                return False
            return recurse(cur.children.get(c), i+1)

        return recurse(self.root, 0)

