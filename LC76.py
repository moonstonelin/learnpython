class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not s or not t:
            return ''

        tdict = {}
        sdict = {}
        for i in range(len(t)):
            if t[i] not in tdict.keys():
                tdict.setdefault(t[i], 0)
                sdict.setdefault(t[i], 0)
            tdict[t[i]] += 1

        count = 0
        start = 0
        ans = ''
        for i in range(len(s)):
            if s[i] not in tdict.keys():
                continue

            sdict[s[i]] += 1
            if sdict[s[i]] <= tdict[s[i]]:
                count += 1

            if count == len(t):
                while start <= i:
                    if s[start] not in tdict.keys():
                        start += 1
                    elif sdict[s[start]] > tdict[s[start]]:
                        sdict[s[start]] -= 1
                        start += 1
                    else:
                        ss = s[start:i+1]
                        if ans == '' or len(ans) > len(ss):
                            ans = ss
                        count -= 1
                        sdict[s[start]] -= 1
                        start += 1
                        break

        return ans

s = Solution()
print s.minWindow('ADOBECODEBANC', 'ABC')
