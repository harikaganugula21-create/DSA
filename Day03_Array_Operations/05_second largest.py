n = list(map(int, input().split()))

largest = n[0]
second = n[0]

for i in n:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)