import sys

if len(sys.argv) > 1:
    # Check if argument is an integer
    for i in range(1, len(sys.argv)):
        if sys.argv[i].isdigit():
                print("Argument is an integer")
                exit()
    # Join all arguments in one string
    result = " ".join(sys.argv[1:])
    # Swap case and reverse the string
    result = result.swapcase()
    print(result[::-1])
    print("")
else:
    print("")