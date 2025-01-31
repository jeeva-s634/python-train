import function
print("Select operation:")
print("1.ADD")
print("2.SUBRACT")
print("3.MULTIPLY")
print("4.DIVISION")
print("5.MODULUS")
while True:
    choice=int(input("Enter the choice(1/2/3/4/5):"))
    if choice in (1,2,3,4,5):
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        if choice==1:
            print(num1,"+",num2,"=",function.addition(num1,num2))
        elif choice==2:
            print(num1,"-",num2,"=",function.subraction(num1,num2))
        elif choice==3:
            print(num1,"*",num2,"=",function.multiplication(num1,num2))
        elif choice==4:
            print(num1,"/",num2,"=",function.division(num1,num2))
        elif choice==5:
            print(num1,"%",num2,"=",function.module(num1,num2))
        else:
            print("Invalid input")
