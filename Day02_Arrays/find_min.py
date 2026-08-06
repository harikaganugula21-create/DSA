arr = list(map(int,input("Enter a elements:" ).split()))

min_element = arr[0]

for i in arr:

    if i < min_element :

        min_element=i
        
print("Minimum Element :",  min_element )        