'''
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。

示例：

输入：
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出：
[null,null,null,null,false,true,true,true]

解释：
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

提示：

1 <= word.length <= 500
addWord 中的 word 由小写英文字母组成
search 中的 word 由 '.' 或小写英文字母组成
最多调用 50000 次 addWord 和 search
'''
class WordDictionary:
    def __init__(self):
        self.dict = [None for _ in range(26)]
        self.tail = False

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.tail = True
            return
        idx = ord(word[0]) - ord('a')
        if not self.dict[idx]:
            self.dict[idx] = WordDictionary()
        self.dict[idx].addWord(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.tail
        if word[0] != '.':
            idx = ord(word[0]) - ord('a')
            if self.dict[idx]:
                return self.dict[idx].search(word[1:])
        else:
            for d in self.dict:
                if d and d.search(word[1:]):
                    return True
        return False