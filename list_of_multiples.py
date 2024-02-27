# https://edabit.com/challenge/BuwHwPvt92yw574zB

def list_of_multiples(num, length):
    return [i*num for i in range(1,length+1)]

print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))