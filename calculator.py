num1  = int(input("Enter the first integer:"))
operator = (input("Enter the your operator:"))
num2  = int(input("Enter the second integer:"))

if (operator=="+"):
    result = (num1+num2)
elif(operator == "-"):
     result =(num1-num2)
elif(operator == "*"):
     result =(num1*num2)
elif(operator == "/"):
     result =(num1/num2)
elif(operator =="//"):
     result =(num1//num2)
else:
    print("NOT VALID")

print(f"The result of the intergers is  :{result}")