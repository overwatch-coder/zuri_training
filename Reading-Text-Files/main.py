# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as file:
        for line in file:
           return line
            
    return "Hello World"


def count_words():
    text = read_file_content("./story.txt")

    dictionary = {}
    # strip whitespace and extra characters
    text = text.strip()

    # split the text into a list
    text = text.split(' ')

    for word in text:
        keys = dictionary.keys()
        if word in keys:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    
    return dictionary

result = count_words()
print(result)