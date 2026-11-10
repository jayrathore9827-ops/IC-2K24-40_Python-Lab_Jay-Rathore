#Take two numbers as input. Print their sum, difference, product, 
#quotient and remainder. Label each output clearly.

a = float(input("Enter the First Number : "))
b = float(input("Enter the Second Number : "))
print("Sum = ",a+b)
print("Diffrence = ",a-b)
print("Product = ",a*b)
if(b ==0):
	print("Cannot compute Quotient and remainder")
else:
	print("Quotient = ",a/b)
	print("Remainder = ",a%b)

# output : 
#Jay Lab-01 % python ArithmeticOperations.py 
#Enter the First Number : 12
#Enter the Second Number : 4
#Sum =  16.0
#Diffrence =  8.0
#Product =  48.0
#Quotient =  3.0
#Remainder =  0.0
