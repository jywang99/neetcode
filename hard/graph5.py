from collections import defaultdict, deque
from typing import List


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        t = 1
        q = deque([beginWord])
        visit = set()
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return t
                visit.add(word)

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nword in adj[pattern]:
                        if nword not in visit:
                            q.append(nword)

            t += 1

        return 0

