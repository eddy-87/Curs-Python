import string


def word_frequency(text):
    text = text.lower()
    for semn in string.punctuation:
        text = text.replace(semn, "")

    cuvinte = text.split()
    frecventa = {}

    for cuvant in cuvinte:
        if cuvant in frecventa:
            frecventa[cuvant] += 1
        else:
            frecventa[cuvant] = 1

    return frecventa


text = "Ana si Maria au plecat la mare. Maria are rau de mare."
print(word_frequency(text))