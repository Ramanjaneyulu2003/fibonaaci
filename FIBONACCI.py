n = int(input())
a = 0
b = 1

print(a, end=" ")

for _ in range(n - 1):
    print(b, end=" ")
    a, b = b, a + b