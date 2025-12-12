def is_palindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False

rezultat = is_palindrom('level')
print (rezultat)