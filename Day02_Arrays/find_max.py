arr = list(map(int,input("Enter a elements:" ).split()))

max_element = arr[0]

for i in arr:

    if i > max_element :

        max_element=i
        
print("Maximum Element :",  max_element )        
