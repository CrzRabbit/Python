class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0
        line = []
        num = ''
        ope = ''
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                num += s[i]
            else:
                print(line, ope, num, s[i])
                if s[i] != ' ':
                    if len(ope):
                        first = line[len(line) - 1]
                        line = line[:-1]
                        if ope == '*':
                            num = first * int(num)
                        if ope == '/':
                            num = int(first / int(num))
                        ope = ''
                    if s[i] == '*' or s[i] == '/':
                        line.append(int(num))
                        ope = s[i]
                    if s[i] == '+' or s[i] == '-':
                        if len(line) >= 2:
                            first = line[0]
                            ope2 = line[1]
                            line.clear()
                            if ope2 == '+':
                                line.append(first + int(num))
                            if ope2 == '-':
                                line.append(first - int(num))
                        else:
                            line.append(int(num))
                        line.append(s[i])
                        ope = ''
                    num = ''
        print(line, ope, num, s[i])
        if len(ope):
            first = line[len(line) - 1]
            line = line[:-1]
            if ope == '*':
                num = first * int(num)
            if ope == '/':
                num = int(first / int(num))
        if len(line) >= 2:
            first = line[0]
            ope2 = line[1]
            line.clear()
            if ope2 == '+':
                line.append(first + int(num))
            if ope2 == '-':
                line.append(first - int(num))
        else:
            line.append(int(num))
        return line[0]

so = Solution()
print(so.calculate('3'))