import re
'''
                    正则表达式
^       [abc]       *           *?          (exp)
$       \W          +           +?          (?<name>exp)
\b      \S          ?           ??          (?:exp)
\d      \D          {n}         {n}?        (?=exp)    
\w      \B          {n,m}       {n,m}?      (?<=exp)
\s      [^abc]      {n,}        {n,}?       (?!exp)
.                                           (?<!exp)
'''
#从开头开始匹配
print(re.match(r"^\w{3}\s", "How are 5_1you51 doing~!"))
#在中间搜索
print(re.search(r"\s\w{3}(?=\s)", "How are 5_1you51 doing~!"))
#替换表达式匹配结果
print(re.sub(r"\s","", "How are 5_1you51 doing~!"))

re.match(r"")