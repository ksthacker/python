
n = int(input())
L = [int(x) for x in input().split()]
st = set(L)
for x in st :
    if L.count(x)==1 :
        print(x,end='')
        break
