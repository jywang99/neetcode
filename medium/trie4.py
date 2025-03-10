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
        

class WordNode:
    def __init__(self):
        self.children: dict[str, WordNode] = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.children:
                n.children[c] = WordNode()
            n = n.children[c]
        n.end = True

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

