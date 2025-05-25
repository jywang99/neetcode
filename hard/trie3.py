from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word = None

    def add_word(self, word: str) -> None:
        n = self
        for c in word:
            if not c in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]
        n.word = word


class WordSearch:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)

        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(board), len(board[0])

        visit, rs = set(), []
        def recurse(r: int, c: int, tn: TrieNode) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or board[r][c] not in tn.children:
                return

            ch = board[r][c]
            nn = tn.children[ch]
            if nn.word:
                rs.append(nn.word)
                nn.word = None

            visit.add((r, c))
            for dr, dc in dirs:
                recurse(r+dr, c+dc, nn)
            visit.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                recurse(r, c, root)

        return rs

