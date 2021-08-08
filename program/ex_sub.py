import re

msg = 'Eli Nan will attend my party tonight. My best friend is Eli Nan'
# pattern = 'Eli Nan'
pattern = r'^Eli'
newstr = 'Roger Tu'
txt = re.sub(pattern, newstr, msg)
if txt!= msg:
    print(f'取代成功: {txt}')
else:
    print(f'取代失敗: {txt}')

