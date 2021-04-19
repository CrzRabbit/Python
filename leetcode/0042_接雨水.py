'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

提示：
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''
class Solution:
    def trap(self, height) -> int:
        stubs = []
        stubindex = []
        ret = 0
        i = 0
        l = len(height)
        if l <= 2:
            return ret
        while i < l:
            if i == 0 and height[i] >= height[i + 1]:
                stub = height[i]
                stubs.append(stub)
                stubindex.append(i)
            elif 0 < i and i < l - 1 and height[i] > height[i - 1] and height[i] >= height[i + 1]:
                stub = height[i]
                stubs.append(stub)
                stubindex.append(i)
            elif i == l - 1 and height[i] > height[i - 1]:
                stub = height[i]
                stubs.append(stub)
                stubindex.append(i)
            i += 1
        print(stubs)
        i = 0
        j = 0
        stubs1 = []
        stubindex1 = []
        l1 = len(stubs)
        if l1 <= 2:
            stubs1 = stubs.copy()
            stubindex1 = stubindex.copy()
        else:
            while i < l1:
                if i == 0 and stubs[i] >= stubs[i + 1]:
                    j = i
                    stub = stubs[i]
                    stubs1.append(stub)
                    stubindex1.append(stubindex[i])
                elif 0 < i and i < l1 - 1 and stubs[i] > stubs[i - 1] and stubs[i] >= stubs[i + 1]:
                    j = i
                    if len(stubs1) == 0:
                        stubs1 += stubs[0: i]
                        stubindex1 += stubindex[0: i]
                    stub = stubs[i]
                    stubs1.append(stub)
                    stubindex1.append(stubindex[i])
                elif i == l1 - 1 and stubs[i] > stubs[i - 1]:
                    if len(stubs1) == 0:
                        stubs1 += stubs[0: i]
                        stubindex1 += stubindex[0: i]
                    j = i
                    stub = stubs[i]
                    stubs1.append(stub)
                    stubindex1.append(stubindex[i])
                i += 1
            stubs1 += stubs[j + 1:]
            stubindex1 += stubindex[j + 1:]
        print(stubs1)
        print(stubindex1)
        for i in range(len(stubindex1) - 1):
            stub = 0
            if height[stubindex1[i]] <= height[stubindex1[i + 1]]:
                stub = height[stubindex1[i]]
            else:
                stub = height[stubindex1[i + 1]]
            print(i, stub)
            for j in range(stubindex1[i] + 1, stubindex1[i + 1]):
                if stub > height[j]:
                    ret += stub - height[j]
        return ret

nums = [0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]
so = Solution()
print(so.trap(nums))