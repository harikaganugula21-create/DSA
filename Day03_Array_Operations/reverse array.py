arr= list(map(int,input("Enter a elements:" ).split()))

rev=0

while(len(arr)<=0):

    digit=arr%10

    rev=rev*10+digit

    arr//10
print(rev)    

