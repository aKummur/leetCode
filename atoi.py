def atoi(s):
    ls = list(s.lstrip())
    if not ls: return 0

    sign = -1 if ls[0] == "-" else 1
    if ls[0] in ['-', '+']: del ls[0]

    i, ret = 0, 0
    while i < len(ls) and ls[i].isdigit():
        ret = ret * 10 + (ord(ls[i]) - ord('0'))
        i += 1

    return max(-2**31, min(sign*ret, 2**31-1))

print(atoi("   -4322345 with words"))