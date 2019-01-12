def is_isogram(word):
    """Determine if word is an isogram"""
    word = list(filter(str.isalpha, word.lower()))

    return len(set(word)) == len(word)

#the filter() method filters the given iterable with the help of a
#function that tests each element in the iterable to be true or not.


#Determine if a word or phrase is an isogram. An isogram (also known as a "nonpattern word") 
#is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.