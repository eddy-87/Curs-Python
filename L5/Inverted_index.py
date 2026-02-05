import string


def inverted_index(documents):
    index_map = {}

    for i, doc in enumerate(documents):
        doc = doc.lower()
        for semn in string.punctuation:
            doc = doc.replace(semn, "")

        cuvinte = set(doc.split())

        for cuvant in cuvinte:
            if cuvant not in index_map:
                index_map[cuvant] = set()
            index_map[cuvant].add(i)

    return index_map


# Test
docs = [
    "pisica a stat pe covor",
    "cainele a stat in ceata",
    "pisica si cainele s-au jucat impreuna"
]
print(inverted_index(docs))