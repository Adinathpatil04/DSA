class Solution(object):
    def reverseVowels(self, s):
        v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

        i = 0
        j = len(s) - 1
        s = list(s)

        while i < j:
            if s[i] not in v:
                i += 1

            if s[j] not in v:
                j -= 1

            if s[i] in v and s[j] in v:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        s = "".join(s)
        return s