# https://edabit.com/challenge/xRMQG4Sxewx5agDRr

def find_highest(lst):
    max = 0
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    list_max = find_highest(lst[1:])
    return lst[0] if lst[0] > list_max else list_max

print(find_highest([0, 12, 4, 87]))
