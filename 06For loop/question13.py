s = "P@#yn26at^&i5ve"

chars = digits = symbols = 0

for ch in s:
    if ch.isalpha():
        chars += 1

    elif ch.isdigit():

        digits += 1

    else:
        symbols += 1

print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)
