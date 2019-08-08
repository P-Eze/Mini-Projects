reset = "Y"
while reset == "Y":
    numb1 = int(input("please type first number"))
    operation = input("please type operation *,+,-,/")
    numb2 = int(input("please type second number"))
    
    if operation == "*":
        print(numb1*numb2)
        reset = input("would you like to do a calculation?Y/N")
    elif operation == "+":
        print(numb1+numb2)
        reset = input("would you like to do a calculation?Y/N")
    elif operation == "-":
        print(numb1-numb2)
        reset = input("would you like to do a calculation?Y/N")
    elif operation == "/":
        print(numb1/numb2)
        reset = input("would you like to do a calculation?Y/N")
    
