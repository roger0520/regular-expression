import re

msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)

print(f'完整號碼是: {phoneNum.group()}')
print(f'完整號碼是: {phoneNum.group(0)}')
print(f'完整號碼是: {phoneNum.group(1)}')
print(f'完整號碼是: {phoneNum.group(2)}')
