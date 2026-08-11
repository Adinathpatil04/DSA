class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0  # word pointer

        while i < len(words):
            # ---------- Phase 1: pack words for one line ----------
            line_words = []
            letters = 0

            while i < len(words) and letters + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                letters += len(words[i])
                i += 1

            # ---------- Phase 2: justify the line ----------
            spaces = maxWidth - letters
            gaps = len(line_words) - 1

            # Case 1: last line OR single word line
            if i == len(words) or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # Case 2: fully justified
                space_each = spaces // gaps
                extra = spaces % gaps

                line = ""
                for j in range(gaps):
                    line += line_words[j]
                    line += " " * (space_each + (1 if j < extra else 0))
                line += line_words[-1]

            result.append(line)

        return result