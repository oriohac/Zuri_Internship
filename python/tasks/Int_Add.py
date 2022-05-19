#Print simple welcome message
print("********WELCOME TO SIMPLE INTEGER CALCULATOR********")

#Receive an input into first_no variable
first_no = input("Enter First Number : ")

#Assign the input to variable a, as an integer
a = int(first_no)

#Receive second input into sec_no variable
sec_no = input("Enter Second Number : ")

#Assign the input to variable b, as an integer
b = int(sec_no)

#Add the two integers held in a and b and assign the result to variable addresult
addresult = int(a + b)

#print the output of the result
print("The Two Numbers Added Equals : "+str(addresult))