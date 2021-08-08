import re

msg = 'tytu@gmail.com.tw'

pattern = r'''(
    [a-zA-Z0-9_.]+  # 使用者帳號
    @               # @符號
    [a-zA-Z0-9-.]+  # 主機域名 domain
    [\.]            # .符號
    [a-zA-Z]{2,4}   # 可能是com或edu....
    ([\.])?         # .符號 也可能無 
    ([a-zA-Z]{2,4})? # 國別
    )'''
eMail = re.findall(pattern, msg, re.VERBOSE)
print(eMail)