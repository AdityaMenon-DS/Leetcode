class Solution(object):
    def fullJustify(self, words, maxWidth):
        ans = []
        i = 0

        while i < len(words):
            j = i
            l = 0

            while j < len(words):
                need = l + len(words[j]) + (j - i)

                if need > maxWidth:
                    break

                l += len(words[j])
                j += 1

            gaps = j - i - 1

            if j == len(words) or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - l
                each = spaces // gaps
                extra = spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (each + (1 if k - i < extra else 0))

                line += words[j - 1]

            ans.append(line)
            i = j

        return ans