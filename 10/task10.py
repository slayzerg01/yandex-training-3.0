k = int(input())
x = []
y = []
for i in range(k):
    a, b = map(int, input().split()) 
    x.append(a)
    y.append(b)

print(f"{min(x)} {min(y)} {max(x)} {max(y)}")
