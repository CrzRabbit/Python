'''
给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。

请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。

工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。

返回分配方案中尽可能 最小 的 最大工作时间 。


示例 1：
输入：jobs = [3,2,3], k = 3
输出：3
解释：给每位工人分配一项工作，最大工作时间是 3 。

示例 2：
输入：jobs = [1,2,4,7,8], k = 2
输出：11
解释：按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。
 

提示：
1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107
'''
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs = sorted(jobs, reverse=True)
        if k >= len(jobs):
            return jobs[0]
        ret = [float('inf')]
        req = [0 for i in range(k)]
        mem = {}
        def required(jobs, req):
            tr = sorted(req, reverse=True)
            tru = (x for x in tr)
            if tru in mem and mem[tru] == jobs:
                print(mem[tru])
                return
            else:
                mem[tru] = jobs
            if len(jobs) == 0:
                req = sorted(req, reverse=True)
                if req[0] < ret[0]:
                    ret[0] = req[0]
                return
            if tr[0] > ret[0]:
                return
            temp = []
            for i in range(k):
                tr = req.copy()
                if tr[i] not in temp:
                    temp.append(tr[i])
                else:
                    continue
                tr[i] += jobs[0]
                required(jobs[1:], tr)
        required(jobs, req)
        return 0 if ret[0] == float('inf') else ret[0]

jobs = [9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935,2420271,4542202]
so = Solution()
print(so.minimumTimeRequired([6518448,8819833,7991995,7454298,2087579,380625,4031400,2905811,4901241,8480231,7750692,3544254], 4))
print(so.minimumTimeRequired(jobs, 9))