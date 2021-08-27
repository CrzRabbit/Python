'''
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
'''
import heapq


class MedianFinder:

    def __init__(self):
        self.heapleft = []
        self.heapright= []

    def addNum(self, num: int) -> None:
        if self.heapright.__len__() == 0 or self.heapleft.__len__() == 0 or num >= self.heapright[0]:
            heapq.heappush(self.heapright, num)
            if self.heapright.__len__() > self.heapleft.__len__() + 1:
                heapq.heappush(self.heapleft, -heapq.heappop(self.heapright))
        else:
            heapq.heappush(self.heapleft, -num)
            if self.heapright.__len__() + 1 < self.heapleft.__len__():
                heapq.heappush(self.heapright, -heapq.heappop(self.heapleft))

    def findMedian(self) -> float:
        if self.heapright.__len__() > self.heapleft.__len__():
            return self.heapright[0]
        elif self.heapright.__len__() < self.heapleft.__len__():
            return -self.heapleft[0]
        else:
            if self.heapleft.__len__() == 0:
                return 0
            return (self.heapright[0] - self.heapleft[0]) / 2
