import sys

if len(sys.argv) < 2:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    sys.exit(1)
else :
    if (sys.argv[1].isdigit() and sys.argv[2].isdigit()):
        nbr1 = int(sys.argv[1])
        nbr2 = int(sys.argv[2])

        print("Sum:         " + str(nbr1 + nbr2))
        print("Difference:  " + str(nbr1 - nbr2))
        print("Product:     " + str(nbr1 * nbr2))
        if nbr1 != 0 and nbr2 != 0:
            print("Quotient:    " + str(nbr1 / nbr2))
            print("Remainder:   " + str(nbr1 % nbr2))
        else:
            print("Quotient:    ERROR (div by zero)")
            print("Remainder:   ERROR (mod by zero)")
    
    else:
        print("AssertionError: only integers")
