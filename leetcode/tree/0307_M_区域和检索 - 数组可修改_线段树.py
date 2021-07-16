'''
给你一个数组 nums ，请你完成两类查询，其中一类查询要求更新数组下标对应的值，另一类查询要求返回数组中某个范围内元素的总和。

实现 NumArray 类：

NumArray(int[] nums) 用整数数组 nums 初始化对象
void update(int index, int val) 将 nums[index] 的值更新为 val
int sumRange(int left, int right) 返回子数组 nums[left, right] 的总和（即，nums[left] + nums[left + 1], ..., nums[right]）


示例：

输入：
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
输出：
[null, 9, null, 8]

解释：
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // 返回 9 ，sum([1,3,5]) = 9
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // 返回 8 ，sum([1,2,5]) = 8

提示：

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
最多调用 3 * 104 次 update 和 sumRange 方法
'''
from typing import List

from leetcode.tools.tree import showTree, buildTree


class NumArray:
    '''
    线段树
    '''
    def __init__(self, nums: List[int]):
        self.len = len(nums)
        '''
        长度为2n
        '''
        self.tree = [0 for _ in range(2 * self.len)]
        '''
        叶子节点即原数据放在[n, 2n - 1]
        '''
        self.tree[self.len:] = nums
        '''
        非叶子节点i左孩子为2 * i, 右孩子为2 * i + 1
        '''
        for i in range(self.len - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
    '''
    从n + index的叶节点开始更新
    '''
    def update(self, index: int, val: int) -> None:
        index = index + self.len
        self.tree[index] = val
        while index > 0:
            left = index
            right = index
            if left % 2 == 0:
                right += 1
            else:
                left -= 1
            index = left // 2
            self.tree[index] = self.tree[left] + self.tree[right]
    '''
    [left, right]区间计算
    '''
    def sumRange(self, left: int, right: int) -> int:
        left += self.len
        right += self.len
        sum = 0
        while left <= right:
            '''
            left为右孩子，计算后右移
            '''
            if left % 2 == 1:
                sum += self.tree[left]
                left += 1
            '''
            right为左孩子，计算后左移
            '''
            if right % 2 == 0:
                sum += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return sum

numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2), numArray.update(1, 2), numArray.sumRange(0, 2))
showTree(buildTree([i for i in range(1, 10)]))


