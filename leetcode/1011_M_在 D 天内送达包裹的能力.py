
'''
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

示例 1：
输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10
请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。

示例 2：
输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

示例 3：
输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
 

提示：

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500
'''
from typing import List
from functools import reduce
from leetcode.tools.time import *
class Solution:
    '''
    每天最少装载max(weights), 最大装载weights总和
    中间执行二分查找
    '''
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        temp = sorted(weights)
        sum = reduce(lambda x, y: x + y, temp)
        left = temp[len(temp) - 1]
        right = sum
        while left < right:
            i = (left + right) // 2
            s = 0
            d = 0
            for j in range(len(weights)):
                s += weights[j]
                if s > i:
                    d += 1
                    s = weights[j]
                    if j == len(weights) - 1:
                        d += 1
                elif s == i:
                    d += 1
                    s = 0
                else:
                    if j == len(weights) - 1:
                        d += 1
            if d <= D:
                right = i
            else:
                left = i + 1
        return right

so = Solution()

weight = [59,429,479,55,157,335,61,433,23,444,42,90,254,97,82,133,116,229,124,331,370,71,296,47,48,229,274,97,284,306,485,486,307,141,205,322,128,59,449,75,79,305,494,119,467,363,25,486,389,463,221,337,55,232,455,356,285,155,484,481,235,406,367,431,308,404,260,244,113,494,194,412,377,49,134,271,98,173,210,42,498,311,251,291,428,277,187,53,467,129,499,53,298,457,390,451,291,182,17,410,479,284,77,204,231,264,220,7,295,42,108,10,113,187,470,165,187,300,244,300,6,154,40,36,67,400,459,403,306,188,251,295,78,25,353,55,223,426,295,154,228,114,363,257,126,27,355,105,246,315,347,355,263,198,358,155,478,158,469,298,447,48,82,455,67,190,122,29,252,300,44,183,7,146,156,108,247,77,364,369,272,230,431,285,80,45,105,444,121,287,376,160,325,236,58,282,57,70,33,103,319,261,277,13,287,97,149,197,366,375,147,124,178,299,464,335,343,159,221,349,450,375,212,357,45,344,148,413,216,201,104,456,318,277,192,493,416,359,24,386,162,340,479,354,358,192,118,283,24,345,302,165,464,487,214,73,229,202,326,175,128,276,209,412,215,128,24,205,99,24,69,202,143,224,429,316,286,316,66,163,45,14,425,72,99,242,13,117,39,52,286,48,41,169,483,424,157,291,405,32,271,140,326,130,37,235,119,164,105,495,98,142,152,158,349,151,427,408,153,272,82,205,420,496,484,14,427,55,361,477,172,218,56,216,281,268,269,438,35,292,288,490,149,197,288,174,334,217,201,141,470,222,46,333,194,464,316,95,136,265,277,42,232,351,466,483,253,94,426,436,396,367,81,144,276,203,165,400,365,458,144,102,277,140,264,193,218,47,209,262,429,410,35,230,53,408,214,481,134,291,404,141,259,54,310,477,348,163,336,290,177,490,360,474,485,156,195,28,427,437,384,269,377,83,170,414,495,148,267,395,89,387,120,273,15,204,161,245,478,416,372,184,206,114,61,213,86,452,487,58,197,362,392,251,45,190,291,260,207,343,273,248,77,71,12,265,219,97,366,261,97,111,81,316,244,348,112,499,392,115,16,207,489,151,117,304,275,277,365,339,252,329,316,384,434,258,306,376,402,405,395,204,34,30,199,188,471,346,420,77,332,266,183,103,446,487,151,24,402,120,59,260,414,219,489,467,176,468,370,206,13,476,210,398,395,348,182,203,376,356,137,230,357,284,63,203,440,442,346,92,362,373,340,24,85,84,42,461,163,89,102,339,42,159,422,459,46,265,179,261,386,384,308,86,375,441,144,342,139,416,339,415,259,106,381,60,258,412,65,75,180,158,452,144,392,121,284,56,26,69,409,170,437,240,83,13,494,161,378,433,204,226,149,177,330,434,240,387,212,344,270,264,318,174,187,276,419,214,174,47,235,89,16,91,218,327,328,312,351,12,490,174,313,95,40,159,278,253,356,182,475,278,299,440,201,205,331,467,187,87,386,434,298,192,25,11,451,333,343,134,165,215,75,51,300,99,497,359,355,248,13,383,83,152,2,448,122,171,348,434,77,63,315,85,198,414,91,190,466,279,246,239,308,489,153,43,121,70,411,31,362,214,419,416,357,449,250,163,352,277,231,335]
print(so.shipWithinDays(weight, 19))

# weight = [3,2,2,4,1,4]
# print(so.shipWithinDays(weight, 3))