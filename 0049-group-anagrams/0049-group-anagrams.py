class Solution(object):
    def groupAnagrams(self, strs):
        d = {}

        for i in strs:
            key = ''.join(sorted(i))

            if key not in d:
                d[key] = []

            d[key].append(i)

        return list(d.values())