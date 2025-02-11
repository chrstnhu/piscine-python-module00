import sys

def operationNumber(argv1, argv2) :
    if (argv1.isdigit() and argv2.isdigit()):
        nbr1 = int(argv1)
        nbr2 = int(argv2)

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


# In terminal
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python operations.py <number1> <number2>")
        print("Example:")
        print("    python operations.py 10 3")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("AssertionError: too many arguments")
        sys.exit(1)
    else :
        operationNumber(sys.argv[1], sys.argv[2])