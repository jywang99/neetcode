from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}

    def add_word(self, word: str) -> None:
        n = self
        for c in word:
            nn = None
            if c in n.children:
                nn = n.children[c]
            else:
                nn = TrieNode()
                n.children[c] = nn
            n = nn


class WordSearch2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
