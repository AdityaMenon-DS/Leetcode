from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return []

        parents = defaultdict(list)
        level = set([beginWord])
        found = False

        while level and not found:
            for w in level:
                if w in words:
                    words.remove(w)

            nxt = set()

            for w in level:
                a = list(w)

                for i in range(len(a)):
                    old = a[i]

                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == old:
                            continue

                        a[i] = c
                        x = "".join(a)

                        if x in words:
                            parents[x].append(w)
                            nxt.add(x)

                            if x == endWord:
                                found = True

                    a[i] = old

            level = nxt

        if not found:
            return []

        ans = []
        path = [endWord]

        def f(w):
            if w == beginWord:
                ans.append(path[::-1])
                return

            for p in parents[w]:
                path.append(p)
                f(p)
                path.pop()

        f(endWord)

        return ans