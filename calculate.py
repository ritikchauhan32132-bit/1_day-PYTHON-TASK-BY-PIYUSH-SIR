print("===Calculator===")


number1 = int(input("Enter 1 number: "))
opr = input("+  -  *  / %: ")
number2 = int(input("Enter 2 number: "))

if(opr in opr):
    
    if(opr == '+'):
        print("Add: ",number1+number2)

    if(opr == '-'):
        print("Substract: ",number1-number2)

    if(opr == '*'):
        print("Multiplication: ",number1*number2)

    if(opr == '/'):
        print("Devided: ",number1/number2)

    if(opr == '%'):
        print("Modulus: ",number1%number2)
else:
    print("Invailed Opretor!")