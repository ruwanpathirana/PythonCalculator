while True:

    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: ! ")
    print("8.Reset    : @ ")

    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if choice == ('!'):
        print("Done. Terminating")
        print(exit())

    elif choice == ('@'):
        break

    elif choice == '+' or choice == '-' or choice == '*' or choice == '^' or choice == '%' or choice=='/':
        a = input("Enter first number: ")
        print(a)
        if a=="0$":   #0$ mean when we not added number to convert into float
            continue
        else:
            b = input("Enter second number: ")
            print(b)
            if a=="#" or b== "#":
                print("Done. Terminating")
                print(exit())

            elif b=="0$":
                continue

            else:
                if choice == ('+'):
                    print(float(a), "+", float(b), "=", float(a) + float(b))

                elif choice == ('-'):
                    print(float(a), "-", float(b), "=", float(a) - float(b))

                elif choice == ('*'):
                    print(float(a), "*", float(b), "=", float(a) * float(b))

                elif choice == ('/'):
                    if b == '0':
                        print("float division by zero")
                        print(float(a), "/", float(b), "= None")

                    else:
                        print(float(a), "/", float(b), "=", float(a) / float(b))

                elif choice == ('^'):
                    print(float(a), "^", float(b), "=", float(a) ** float(b))

                else:
                    print(float(a), "%", float(b), "=", float(a) % float(b))

    else:
        print("Unrecognized operation")
        break

