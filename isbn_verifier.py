import re

def check_isbn_formula(digits):
    numbers_to_mult = list(map(int, digits))
    return sum([factors[0] * factors[1] for factors in zip(numbers_to_mult, range(10,0,-1))]) % 11 == 0

def verify(isbn):
    stripped_isbn = isbn.replace("-", "")
    if not re.compile("[0-9]{9}([0-9]|X)$").match(stripped_isbn):
        return False
    else:
        digits = list(stripped_isbn)
        if digits[-1] == 'X':
            digits[len(digits)-1] = '10'
        return check_isbn_formula(digits)

#The method strip() returns a copy of the string in which all chars have been
#stripped from the beginning and the end of the string (default whitespace characters).

#The ISBN-10 verification process is used to validate book identification numbers. 
#These normally contain dashes and look like: 3-598-21508-8