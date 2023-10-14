
# find longest one 
def lon_word(sentence):
    word=sentence.split()
    lon_word=max(word,key=len)
    return lon_word
sentence="the quickee brownee fox jumps over the lazy "
print(lon_word(sentence))