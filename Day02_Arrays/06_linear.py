arr = list(map(int,input("Enter a elements:" ).split()))

target=int(input("Enter Target Value :"))

found=False

for i in range(len(arr)):

    if arr[i]==target:

        print("Value at index", arr[i])

        found=True

        break

if not found:

    print("Element not found") 