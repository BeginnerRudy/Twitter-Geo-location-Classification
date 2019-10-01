import string

def clear_punctuation(s):
    clear_string = ""
    for symbol in s:
        if symbol not in string.punctuation:
            clear_string += symbol
    return clear_string


print(clear_punctuation('"How can you remove full-stops, hashtags, symbols, commas, hyphen, semicolon etc from dataset using python for sentiment analysis?Commas, hyphen, semicolon, hash tags , punctuations are to be removed') )


# The aforementioned code removes most punctuation symbols (e.g. !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~). Nevertheless, if you want to remove specific items you may try the following:
string_punctuation =  ".#,_;"

def remove_punctuation(s):
    no_punct = ""
    for letter in s:
        if letter not in string_punctuation:
            no_punct += letter
    return no_punct

print(clear_punctuation('"test!!!How can you remove full-stops, hashtags, symbols, commas, hyphen, semicolon etc from dataset using python for sentiment analysis?Commas, hyphen, semicolon, hash tags , punctuations are to be removed') )

