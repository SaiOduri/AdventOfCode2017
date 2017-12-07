# PART 1
def InverseCaptcha(Digits):
    sum = 0
    for i in range(len(Digits)):
        if Digits[i] == Digits[(i + 1) % len(Digits)]:
            sum += int(Digits[i])
    return sum

# PART 2
def InverseCaptcha2(Digits):
    sum = 0
    for i in range(len(Digits)):
        if Digits[i] == Digits[(i + len(Digits)/2) % len(Digits)]:
            sum += int(Digits[i])
    return sum
