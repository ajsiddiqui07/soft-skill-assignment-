again ='y'
while again =='y'  :
    value_1 = int(input("Enter first value : "))
    value_2 = int(input("Enter second value : "))
    print("""1. enter 1 for sum
            2. enter 2 for sub
            3. enter 3 for mult
            4. enter 4 for div """)
    choice=int(input("choose 1 to 4 num for perform specific task : "))
    if choice==1:
        print(value_1+value_2)
    elif choice==2:
        print(value_1-value_2)
    elif choice==3:
        print(value_1*value_2)
    elif choice==4:
        print(value_1/value_2)
    again=input("do you want to con? y or n : ")
       
