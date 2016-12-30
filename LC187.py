class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []

        visited = set()
        mapping = {'A': 0, 'C': 1, 'T': 2, 'G': 3}

        num = 0
        k = (1 << 20) - 1
        for i in range(0, 9):
            num = (num << 2) + mapping[s[i]]

        ans = []
        for i in range(9, len(s)):
            num = ((num << 2) + mapping[s[i]]) & k
            ss = s[i-9:i+1]
            if num not in visited:
                visited.add(num)
            else:
                if ss not in ans:
                    ans.append(ss)

        return ans

s = Solution()
print s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')