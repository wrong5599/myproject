sum=0;
rem=0;
num=int(input("Enter Number which you want to check:"))
while num>0:
	rem=num%10;
	num=num//10;
	sum=(sum*10)+rem;	#this is the comment
if(num==sum):
	print("Given no is Palamdrom")
else:
	print("Given no is not a Palamdrom")
