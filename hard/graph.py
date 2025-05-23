from typing import List
from collections import defaultdict, deque


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        rs = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return rs
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nword in adj[pattern]:
                        if nword not in visit:
                            visit.add(nword)
                            q.append(nword)
            rs += 1

        return 0
