def repeated(a, b):

    result = 0
    word = b

    while True:
        if word in a:
            word += b
            result += 1
        else: 
            break
    if word == b:
        return 0

    return result

print(repeated("pokpokpok", 'po'))


