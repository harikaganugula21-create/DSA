arr = list(map(int,input("Enter a Elements :").split()))

sum_of_elements=0

count = 0

for i in arr:

    sum_of_elements+=i

    count += 1

print("Average of Array :",sum_of_elements/count)    