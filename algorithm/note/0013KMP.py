'''
KMP
'''
class KMP:
    def __init__(self, p):
        self.p = p
        self.pmt = [0 for _ in range(len(p))]
        j = 0
        for i in range(1, len(p)):
            while j >= 0 and p[i] != p[j]:
                j = self.pmt[j - 1] if j != 0 else -1
            j += 1
            self.pmt[i] = j

    def search(self, s):
       j = 0
       for i in range(len(s)):
           while j >= 0 and s[i] != self.p[j]:
               j = self.pmt[j - 1] if j != 0 else -1
           j += 1
           if j == len(self.p):
               return i - j + 1
       return len(s)


kmp = KMP('abcabacd')
print(kmp.search('abaabcabacdcde'))