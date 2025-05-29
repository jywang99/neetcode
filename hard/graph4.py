from collections import defaultdict, deque
from typing import List


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(set)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].add(word)

        visit = set()
        q = deque([beginWord])
        rs = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return rs
                visit.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nword in adj[pattern]:
                        if nword in visit:
                            continue
                        q.append(nword)
            rs += 1

        return 0

