def stringy(size):

    length = list(size)
    res = ""

    for i, val in enumerate(length, start = 1):
        if i%2 == 1:
            res += "1"
        else:
            res+="0"

    return res
print(stringy("Diana"))

