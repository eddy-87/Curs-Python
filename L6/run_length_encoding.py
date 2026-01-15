def run_length_encoding(text):
    if text == "":
        return ""

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    result += text[-1] + str(count)
    return result

text = "aaabbbbcccdde"
print(run_length_encoding(text))
