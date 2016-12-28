#实现分页显示。给了以下一些输入数据，要求将以下行分页显示，每页12行，其中每行已经按score排好序，分页显示的时候如果有相同host id的行，则将后面同host id的行移到下一页。
class Solution(object):
    def display(self, lines):
        ans = []

        if not lines:
            return ans

        lines.remove(lines[0])

        count = 12
        ids = set()
        buf = []
        page = []

        start = 0
        while start < len(lines) or len(buf) > 0:
            for l in buf:
                if len(page) == count:
                    break
                curid = l.split(',')[0]
                if curid not in ids:
                    page.append(l)
                    ids.add(curid)

            for l in page:
                buf.remove(l)

            while start < len(lines) and len(page) < count:
                l = lines[start]
                curid = l.split(',')[0]
                if curid in ids:
                    buf.append(l)
                else:
                    page.append(l)
                    ids.add(curid)
                start += 1

            ans.append(page)
            ids.clear()
            page = []

        return ans

s = Solution()
lines = ["host_id,listing_id,score,city", "1,28,300.1,SanFrancisco", "4,5,209.1,SanFrancisco",
"20,7,208.1,SanFrancisco","23,8,207.1,SanFrancisco", "16,10,206.1,Oakland", "1,16,205.1,SanFrancisco",
"6,29,204.1,SanFrancisco", "7,20,203.1,SanFrancisco", "8,21,202.1,SanFrancisco", "2,18,201.1,SanFrancisco",
"2,30,200.1,SanFrancisco", "15,27,109.1,Oakland", "10,13,108.1,Oakland", "11,26,107.1,Oakland",
"12,9,106.1,Oakland", "13,1,105.1,Oakland", "22,17,104.1,Oakland", "1,2,103.1,Oakland", "28,24,102.1,Oakland",
"18,14,11.1,SanJose", "6,25,10.1,Oakland","19,15,9.1,SanJose","3,19,8.1,SanJose",
"3,11,7.1,Oakland","27,12,6.1,Oakland","1,3,5.1,Oakland","25,4,4.1,SanJose", "5,6,3.1,SanJose","29,22,2.1,SanJose",
"30,23,1.1,SanJose"
]

print s.display(lines)
