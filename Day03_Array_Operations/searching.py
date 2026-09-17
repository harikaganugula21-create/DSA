arr=list(map(int,input().split()))

target=int(input("enter target element:"))

found=False

for i in range(len(arr)):


    if arr[i]==target:

        print(arr[i])

        found=True

if not found:
    print("not element is found")        



