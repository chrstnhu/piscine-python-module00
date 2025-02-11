import sys
import string

# Prints the list of words in string that contains more than N non-punctuation characters.
def filterword() :
    if (not isinstance(sys.argv[1], str)) or sys.argv[1].isdigit():
        print("ERROR : need a STRING for argv[1]")
        sys.exit()
    elif not sys.argv[2].isdigit():
        print("ERROR : need a DIGIT for argv[2]")
        sys.exit()
    text = sys.argv[1] 
    max_nbr = int(sys.argv[2])

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    split_text = clean_text.split(" ")

    # Find word lenght > max_nbr
    result = []
    for word in split_text:
        if len(word) >= max_nbr:
            result.append(word)
    print(result)

# Main
if __name__ == "__main__":
    if len(sys.argv) == 3:
       filterword()
    else:
        print("Usage : python3 filterwords.py [string] [int]")
    