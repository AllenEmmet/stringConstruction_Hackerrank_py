def stringConstruction(s):
    store = []
    arr = list(s)
    cost = 0
    for letter in s:
        if letter not in store:
            cost += 1
            store.append(letter)
    return cost


