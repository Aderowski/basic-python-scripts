# https://edabit.com/challenge/2zKetgAJp4WRFXiDT

def number_length(number):
    length = 1 
    while True:
        if number >= 10:
            length+=1
            number/=10
        elif number < 10:
            return length

print(number_length(5000))