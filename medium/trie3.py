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
            if c not in n.children:
                n.children[c] = WordNode()
            n = n.children[c]
        n.end = True

    def search(self, word: str) -> bool:
        def recurse(n: Optional[WordNode], i: int) -> bool:
            if not n:
                return False
            if i == len(word):
                return n is not None and n.end

            c = word[i]
            if c == ".":
                for nn in n.children.values():
                    if recurse(nn, i+1):
                        return True
                return False
            
            return recurse(n.children.get(c), i+1)

        return recurse(self.root, 0)

