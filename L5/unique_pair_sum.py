def unique_pair_sum(numbers, target):
    perechi = set()
    vazute = set()

    for num in numbers:
        complement = target - num
        if complement in vazute:
            pereche = (min(num, complement), max(num, complement))
            perechi.add(pereche)
        vazute.add(num)

    return perechi


# Test
numbers = [1, 2, 3, 4, 3, 5, 6]
target = 7
print(unique_pair_sum(numbers, target))