from sys import stdin
for a in stdin:
    temp = ''
    f = 1
    for i in range(len(a)):
        if (f == 0):
            f = 1
        else:
            if (a[i]=='-' and a[i+1]=='>'):
                temp+='.'
                f=0
            elif(a[i]=='/'and a[i+1]=='/'):
                temp+= a[i:]
                break;
            else:
                temp += a[i]
    print(temp)
