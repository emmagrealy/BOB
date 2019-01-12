def hey(phrase):
    phrase = phrase.strip()
    if not phrase:
        return "Fine. Be that way!"
    if phrase.endswith("?"):
        if phrase.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    #returns “True” if all characters in the string are uppercase    
    if phrase.isupper():
        return "Whoa, chill out!"
    return "Whatever."

#completed

#Bob is a lackadaisical teenager. In conversation, his responses are very limited.
#Bob answers 'Sure.' if you ask him a question.
#He answers 'Whoa, chill out!' if you yell at him.
#He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
#He says 'Fine. Be that way!' if you address him without actually saying anything.
#He answers 'Whatever.' to anything else.