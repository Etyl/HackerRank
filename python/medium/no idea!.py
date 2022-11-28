(n,m) = tuple(map(int,input().split()))
l = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

happiness = 0
for x in l:
    happiness += (x in A) - (x in B)
print(happiness)
