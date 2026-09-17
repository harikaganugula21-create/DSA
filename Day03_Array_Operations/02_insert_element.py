arr = [10, 20, 30, 40, 60]

index = 4
value = 50

# Create extra space
arr += [0]

# Shift elements to the right
for i in range(len(arr) - 1, index, -1):
    arr[i] = arr[i - 1]

# Insert value
arr[index] = value

print(arr)
