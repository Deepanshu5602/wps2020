str1= input()
str2= input()
lst = []
if (len(str1)!= len(str2)):
    print('NO')
else:
    for i in range(len(str1)):
        h =ord(str1[i])- ord(str2[i])
        lst.append(h)
    flag =1
    for i in range(1, len(lst)-1):
        if lst[i]>0:
            flag=0
            break
    if flag!=1:
        print('NO')
    else:
        print('YES')