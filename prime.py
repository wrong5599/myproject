num= int(input("Enter the Number"));
if num>1:
	if(num==2):
		print(str(num)+" is a Prime Number");
		print("{} is a prime nos".format(num));
	else:
		for i in range(2,num): 	
			if(num%i)==0:
				print(str(num)+" is not a Prime Number");
			else:
				print(str(num)+" is a Prime Number");
			break;
else:
	print("Prime No. is Greater than 2, you press invalid Nos.");	