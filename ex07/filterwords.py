import sys
import string

# Prints the list of words in string that contains more than N non-punctuation characters.
if len(sys.argv) == 3:
    if (not isinstance(sys.argv[1], str)) or sys.argv[1].isdigit() or (not sys.argv[2].isdigit()):
        print("ERROR")
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
else:
    print("ERROR")
