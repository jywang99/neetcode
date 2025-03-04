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


class WordNode:
    def __init__(self) -> None:
        self.children: dict[str, WordNode] = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        n = self.root
        for c in word:
            if not n.children.get(c):
                n.children[c] = WordNode()
            n = cast(WordNode, n.children[c])
        n.end = True

    def search(self, word: str) -> bool:
        def recurse(cur: WordNode, i: int) -> bool:
            if i == len(word):
                return cur.end

            c = word[i]
            if c == '.':
                for n in cur.children.values():
                    if recurse(n, i+1):
                        return True
                return False

            if c not in cur.children:
                return False
            return recurse(cur.children[c], i+1)

        return recurse(self.root, 0)

