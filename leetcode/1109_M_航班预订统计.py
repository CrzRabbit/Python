'''
这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。


示例 1：

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]

示例 2：

输入：bookings = [[1,2,10],[2,2,15]], n = 2
输出：[10,25]
解释：
航班编号        1   2
预订记录 1 ：   10  10
预订记录 2 ：       15
总座位数：      10  25
因此，answer = [10,25]

提示：

1 <= n <= 2 * 104
1 <= bookings.length <= 2 * 104
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 104
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    线段树
    '''
    @printTime()
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        class SegmentTree:
            def __init__(self, data):
                self.data = data
                self.n = len(data)
                self.tree = [0 for _ in range(self.n << 2)]
                self.mark = [0 for _ in range(self.n << 2)]
                self.build(1, self.n, 1)

            def build(self, l, r, p):
                if l == r:
                    self.tree[p] = self.data[l - 1]
                    return
                mid = (l + r) >> 1
                self.build(l, mid, p << 1)
                self.build(mid + 1, r, (p << 1) + 1)
                self.tree[p] = self.tree[p << 1] + self.tree[(p << 1) + 1]

            def push_down(self, p, len):
                self.mark[p << 1] += self.mark[p]
                self.mark[(p << 1) + 1] += self.mark[p]
                self.tree[p << 1] += self.mark[p] * (len - (len >> 1))
                self.tree[(p << 1) + 1] += self.mark[p] * (len >> 1)
                self.mark[p] = 0

            def update(self, l, r, d):
                def update(l, r, d, cl, cr, p):
                    if cl > r or cr < l:
                        return
                    elif cl >= l and cr <= r:
                        self.tree[p] += (cr - cl + 1) * d
                        if cr > cl:
                            self.mark[p] += d
                    else:
                        mid = (cr + cl) >> 1
                        self.push_down(p, (cr - cl + 1))
                        update(l, r, d, cl, mid, p << 1)
                        update(l, r, d, mid + 1, cr, (p << 1) + 1)
                        self.tree[p] = self.tree[p << 1] + self.tree[(p << 1) + 1]
                update(l, r, d, 1, self.n, 1)

            def query(self, l, r):
                def query(l, r, cl, cr, p):
                    if cl > r or cr < l:
                        return 0
                    elif cl >= l and cr <= r:
                        return self.tree[p]
                    else:
                        mid = (cl + cr) >> 1
                        self.push_down(p, (cr - cl + 1))
                        return query(l, r, cl, mid, p << 1) + query(l, r, mid + 1, cr, (p << 1) + 1)
                return query(l, r, 1, self.n, 1)
        st = SegmentTree([0 for _ in range(n + 1)])
        for b in bookings:
            st.update(b[0], b[1], b[2])
        ans = []
        for i in range(1, n + 1):
            ans.append(st.query(i, i))
        return ans
    '''
    差分 + 前缀和
    '''
    @printTime()
    def _1corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0 for i in range(n)]
        for b in bookings:
            nums[b[0] - 1] += b[2]
            if b[1] < n:
                nums[b[1]] -= b[2]
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums

bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
# Solution().corpFlightBookings(bookings, n)
Solution()._1corpFlightBookings(bookings, n)