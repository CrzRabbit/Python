'''
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。

示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        temp = []
        n = 0
        for word in words:
            print(temp, n)
            if n + len(temp) + len(word) > maxWidth:
                if len(temp) > 1:
                    x = (maxWidth - n) // (len(temp) - 1)
                    y = (maxWidth - n) % (len(temp) - 1)
                tret = temp[0]
                for i in range(1, len(temp)):
                    tret += ' ' * x
                    if y:
                        tret += ' '
                        y -= 1
                    tret += temp[i]
                ret.append(tret + ' ' * (maxWidth - len(tret)))
                temp.clear()
                temp.append(word)
                n = len(word)
            elif n + len(temp) + len(word) == maxWidth:
                temp.append(word)
                tret = temp[0]
                for i in range(1, len(temp)):
                    tret += ' ' + temp[i]
                ret.append(tret)
                temp.clear()
                n = 0
            else:
                temp.append(word)
                n += len(word)
        if len(temp):
            tret = temp[0]
            for i in range(1, len(temp)):
                tret += ' ' + temp[i]
            ret.append(tret + ' ' * (maxWidth - len(tret)))
        return ret

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Solution().fullJustify(words, maxWidth)