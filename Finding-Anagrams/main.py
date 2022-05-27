# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # strip off extra whitespaces
    word = word.strip().replace(' ', '')
    anagram = anagram.strip().replace(' ', '')

    # convert the word and anagram to a list
    word = list(word.lower())
    anagram = list(anagram.lower())

    # sort the word and anagram
    word = sorted(word)
    anagram = sorted(anagram)
    
    # Check if they are the same
    if (word == anagram):
        return True
    else:
        return False
    

result = find_anagram('William Shakespeare', 'I am a weakish speller')
print(result)

