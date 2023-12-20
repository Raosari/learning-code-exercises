counter = 1
def ince(maxium):
    print(maxium)
    if maxium > 3:
        return 'done'
    maxium += 1
    return ince(maxium)

ince(counter)