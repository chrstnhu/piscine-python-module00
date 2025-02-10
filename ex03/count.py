import sys

# Analyze the text (upper, lower, punctuation, space)
def text_analyzer(string = None):
    # Docstring [ print(text_analyzer.__doc__) ]
    """ 
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    
    if string is None:
        print("What is the text to analyze?")
        string = input(">>")
    if not isinstance(string, str):
        print("AssertionError: Argument is not a string")
    else:
        upperCase = 0
        lowerCase = 0
        space = 0
        digit = 0
        punctuation = 0

        # Count the number of upper, lower, punctuation and space
        for i in range(len(string)):
            if string[i].isprintable():
                if string[i].isupper():
                    upperCase += 1
                elif string[i].islower():
                    lowerCase += 1
                elif string[i].isspace():
                    space += 1
                elif string[i].isdigit():
                    digit += 1
                else:
                    punctuation += 1

        # Count the number of printable characters
        printable = upperCase + lowerCase + space + digit + punctuation

        print("The text contains " + str(printable) + " printable character(s):")
        print("- " + str(upperCase) + " upper letter(s)")
        print("- " + str(lowerCase) + " lower letter(s)")
        print("- " + str(punctuation) + " punctuation mark(s)")
        print("- " + str(space) + " space(s)")

# In terminal
if __name__ == "__main__":
    # Check the number of argument
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else :
        print("AssertionError: more than one argument is provided")