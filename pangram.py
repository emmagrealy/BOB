from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

#issubset = Returns a Boolean stating whether the set is contained in the specified set or iterable. 
#(Required. Iterable to be compared against the set.)
#returns a boolean 
def is_pangram(string):
    return ALPHABET.issubset(string.lower())


#Determine if a sentence is a pangram. A pangram is a sentence using every letter of the alphabet at least once.