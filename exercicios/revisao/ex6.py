a, b = map(int, input().split())

print("[", end=" ")
for i in range(a, b, -1):
    print(i, end=" ")
print("]")