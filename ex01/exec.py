import sys

# Check if argument is passed
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].isdigit():
            try :
                number = int(sys.argv[i])
                print("Argument is an integer")
                exit()
            except ValueError:
                print("Argument is not an integer")
                exit()
    result = " ".join(sys.argv[1:])
    result = result.swapcase()
    print(result[::-1])
    print("")
else:
    print("")