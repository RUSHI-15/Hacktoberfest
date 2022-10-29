
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    r = (a+b)&1
    k = (c+d)&1
    if r == k:
        print("Yes")
    else:
        print("No")
