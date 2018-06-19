sum=0;
rem=0;
n=0;
while True:
	try:
		num=input("Enter Number which you want to check:")
		num=int(num)
		n=num
		break
	except ValueError:
		print("No valid Integer, Please try again")
print("Great, you successfuly enter valid Integer")
while n>0:
	rem=n%10;
	n=n//10;
	sum=(sum*10)+rem;	#this is the comment
if(num==sum):
	print(sum);
	print("Given no is Palamdrom")
else:
	print(sum);
	print("Given no is not a Palamdrom")
