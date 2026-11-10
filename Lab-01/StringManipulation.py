#5. String Manipulation
#Take a full name as input. Print it in uppercase, in lowercase, 
#reversed, and print its length. Use at least three different string methods.

name = input("Enter your full name : ")
print("In Upper case : ",name.upper())
print("In Lower case : ",name.lower())
print("Reversed : ",name[::-1])
print("Total Length : ",len(name))

#(base) Jay Lab-01 % python StringManipulation.py 
#Enter your full name : Jay Rathore
#In Upper case :  AISHWARYA KUMAR SINGH
#In Lower case :  aishwarya kumar singh
#Reversed :  hgniS ramuK ayrawhsiA
#Total Length :  21
