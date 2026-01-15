def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

sentence = "soricel un cu joaca se pisica"
print(reverse_words(sentence))
