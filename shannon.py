# Shannon decoder
# Sample input:
# 4
# А 0
# B 10
# C 110
# D 111
# 00101101110010110
# Sample output:
# AABCDAABC

alph_len = int(input('Длина алфавита:'))
codes = {}
for i in range(alph_len):
    code_pair = input().split()
    codes[code_pair[1]] = code_pair[0]
message = input()

result = ''
while len(message) > 0:
    for code in codes:
        if message.startswith(code):
            result += codes[code]
            message = message[len(code):]
            break
print(result)
