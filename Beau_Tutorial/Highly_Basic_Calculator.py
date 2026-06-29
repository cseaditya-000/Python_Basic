a=str(input("Enter the operation you would like to perfrom out of +, -, *, / : "))
number_1=float(input("Enter the first number: "))
number_2=float(input("Enter the second number: "))
if a=="+":
    print(number_1+number_2)
elif a=="-":
    print(number_1-number_2)
elif a=="*":
    print(number_1*number_2)
elif a=="/":
    print(number_1/number_2)
else:
    print("Invalid Operation")