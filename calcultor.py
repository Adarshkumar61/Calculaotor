def calculator():
    user = float(input(f"Enter your 1st number: "))
    op = input(f"What do u want to do(+, -, *, /) : ")
    user1= float(input(f"Enter your 2nd number: "))
    if op == "+" :
        summ = user + user1
        print(f"The sum of {user} and {user1} is: ", summ)
    elif op == "-" :
        minus = user - user1
        print(f"The substraction of {user} and {user1} is: ", minus)
    elif op == "*" :
        mul = user * user1
        print(f"The multipication of {user} and {user1} is: ", mul)
    elif op == "/" :
        if user1 == 0:
            print("2nd entry cant be zero")
        else:
            divide = user/user1
            print(f"The division of {user} and {user1} is: ", divide)
    else:
        print("Invalid!")
calculator()