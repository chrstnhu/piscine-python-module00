import sys

# Check if there is more than one argument
if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 2:
    # Check if the argument is a number
    if sys.argv[1].isdigit():
        number = int(sys.argv[1])
        if number == 0:
            print("I'm Zero.")
        elif (number % 2) == 0:
            print("I'm Even.")
        else :
            print("Im Odd.")
    else :
        print("AssertionError: argument is not an integer")
    
else :
    print("")