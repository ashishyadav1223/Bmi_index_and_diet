import re
data=['9878654321','1234567895','987654567','8765432198','67548943']
for value in data:
   if re.findall(r'^[8-9]{1}[0-9]{9}',value)and len (value)==10:
        print(value)
   else:
        print("invalid")
import re
data="ashish virar 29-08-2005 and raj nalasopara 5-09-2006 gayatri vasai 7-4-2003"
pattern=r"\d{2}-?\d{2}-?\d{4}"
matchs=re.findall(pattern,data)
print(matchs)

'''import re
data="my email addresses are shantanu@gmail.com and ashishmydav@gmail.com"
pattern=r'\w+@\w+\.'
email=re.findall(pattern,data)
print(email)

import re
data="ashish is my student\n and he is really good boy"
pattern=r'.'
match=re.findall(pattern,data)
print(data)

import re
data="hi shrutikashsh is am ashishshshsh"
pattern=r'sh+'
match=re.findall(pattern,data)
print(match)

import re
data="ritika my love"
pattern=r"^ritika"
match=re.finditer(pattern,data)
for match in match:
    print(match.group())

import re
text="hi i am 18 year old"
patter=r"[^0-9]"
match=re.findall(patter,text)
print(match)

import re
pattern=r"\d+$"
text="the code is 123 and find code is 1999"
matches=re.findall(pattern,text)
print(matches)
'''
