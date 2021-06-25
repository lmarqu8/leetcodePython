class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort(key=len)
        if len(strs[0]) == 0: return ""
        lcp = ""
        temp = strs[0][0]
        size = len(strs)
        lettercount = len(strs[0])

        for x in range(lettercount):
            for word in strs:
                if (temp[x] != word[x]):
                    return lcp
            lcp = temp
            if (x == lettercount - 1): return lcp
            temp += word[x + 1]
        return lcp