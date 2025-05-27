from collections import defaultdict, deque
from typing import List


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        q = deque([beginWord])
        visit = set()
        rs = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word == endWord:
                    return rs
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nword in adj[pattern]:
                        if nword not in visit:
                            q.append(nword)
            rs += 1

        return 0

