from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            w, d = q.popleft()

            if w == endWord:
                return d

            a = list(w)

            for i in range(len(a)):
                old = a[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == old:
                        continue

                    a[i] = c
                    x = "".join(a)

                    if x in words:
                        words.remove(x)
                        q.append((x, d + 1))

                a[i] = old

        return 0