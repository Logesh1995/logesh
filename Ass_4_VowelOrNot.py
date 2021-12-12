
def vowelcheck(c):
    v = ["a", "e", "i", "o", "u"]

    for i in v:
        if i == c:

            return "vowel"
            break
    else:
        return "not a vowel"

c = input("Enter a letter:")
print(vowelcheck(c))
