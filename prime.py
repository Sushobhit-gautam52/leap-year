# prime number
count=0
n=int(input("enter anumber"))
for i in range(1,n+1):
    if n%i==0:
       count=count+1
if count==2:
    print("prime number")
else:
    print("not a prime number")

