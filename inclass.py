# 1.18.11

# take a cardinal number and give us the ordinal version

def ordinalnum(number):
    last_digit = abs(number) % 10
    last_two = abs(number) % 100
    number = str(number)
    text = number + "th" # a sensible default

    if (last_digit == 1) & (last_two != 11):
        text = number + "st"
    elif (last_digit == 2) & (last_two != 12):
        text = number + "nd"
    elif (last_digit == 3) & (last_two != 13):
        text = number + "rd"

    return text

# a test
#for i in range(1,11):
#    print ordinalnum(i)
