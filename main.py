import re
matn = ["12asd,hfj45,s1,h34,21s"]

text = []
for i in matn:
    text.extend(map(int,re.findall(r'\d+',i)))
text.sort()
print(text)