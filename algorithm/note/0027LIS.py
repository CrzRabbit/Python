'''
LIS nlog(n)
'''
import bisect


class LIS:
    def __init__(self, nums):
        self.nums = nums

    def get(self):
        mem = [self.nums[0]]
        for num in self.nums:
            if num > mem[-1]:
                mem.append(num)
            else:
                mem[bisect.bisect_left(mem, num)] = num
        return len(mem)

lis = LIS([4, 8, 9, 5, 6, 7, 2])
print(lis.get())