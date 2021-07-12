
def substring(s):
    length =len(s)
    ss = set()
    for i in range(length):
        n = ''
        for j in range(i,length):
            n = n + s[j]
            ss.add(n)

    return len(ss)


s  = input()

print(substring(s))
