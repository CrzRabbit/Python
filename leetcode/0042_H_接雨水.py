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
    '''
    回溯
    桩, height中的凸出部：
        i == 0 and height[i] >= height[i + 1] and height[i] != 0
        0 < i and i < l - 1 and height[i] > height[i - 1] and height[i] >= height[i + 1]
        i == l - 1 and height[i] > height[i - 1]
    1. 如果当前的桩不高于上一个桩，记录当前桩的值，位置，和上一个桩之间的雨水量
    2. 如果当前桩高于上一个桩，从上一个桩开始往回查找，如果有高于上一个的桩，清空该桩与上一个桩之间的记忆。
        遍历过上一个桩之前的所有桩或者有高于当前的桩停止。将查到的桩作为上一个桩与当前桩记录当前桩的值，位置，雨水量
    '''
    def trap(self, height) -> int:
        def getValue(start, end, stub):
            ret = 0
            for i in range(start, end):
                if height[i] < stub:
                    ret += stub - height[i]
            return ret
        stubs = []
        stubindex = []
        values = []
        stub = 0
        ret = 0
        i = 0
        l = len(height)
        if l <= 2:
            return ret
        while i < l:
            print(stubs, stubindex, values)
            if i == 0 and height[i] >= height[i + 1] and height[i] != 0:
                stub = height[i]
                stubs.append(stub)
                stubindex.append(i)
            elif (0 < i and i < l - 1 and height[i] > height[i - 1] and height[i] >= height[i + 1]) or (i == l - 1 and height[i] > height[i - 1]):
                if stub != 0:
                    if stub >= height[i]:
                        value = getValue(stubindex[len(stubindex) - 1] + 1, i, height[i])
                    else:
                        for j in range(len(stubs) - 2, -1, -1):
                            if stubs[j] > stub:
                                stubs = stubs[:j + 1]
                                stubindex = stubindex[:j + 1]
                                stub = stubs[j]
                                for k in range(len(values) - 1, j - 1, -1):
                                    ret -= values[k]
                                values = values[:j]
                                if stubs[j] >= height[i]:
                                    break
                        if stub >= height[i]:
                            value = getValue(stubindex[len(stubindex) - 1] + 1, i, height[i])
                        else:
                            value = getValue(stubindex[len(stubindex) - 1] + 1, i, stub)
                    ret += value
                    stub = height[i]
                    stubs.append(stub)
                    stubindex.append(i)
                    values.append(value)
                else:
                    stub = height[i]
                    stubs.append(stub)
                    stubindex.append(i)
            i += 1
        print(stubs, stubindex, values)
        return ret

nums = [1,0,5,0,7,3,1,5,5,0,7,6,8,4,0,5]
so = Solution()
print(so.trap(nums))