q = int(input())
for i in range(q):
    s = input()
    t = input()
    lst = []
    for i in range(len(s)):
        if(ord(s[i]))>ord(t[i]):
            val = 26 - ord(s[i])+ord(t[i])
        else:
            val = ord(t[i])-ord(s[i])
        lst.append(val)
    lst = set(lst)
    if(len(lst)==1):
        if(ord(s[0]))>(ord(t[0])):
            val= 26-ord(s[0])+ord(t[0])
        else:
            val = ord(t[0])-ord(s[0])
        print(val)
    else:
        print(-1)