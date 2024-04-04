def sc(num1 :int ,num2:int, operator: chr)->int:
    if(operator=='+'):
        return num1+num2
    elif(operator=='-'):
        return num1-num2
    elif(operator=='/'):
        return num1/num2
    else:
        return num1*num2  
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
opr = str(input("Enter the opreator :"))
print(sc(num1,num2,opr))