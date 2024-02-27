farey_list = []

def farey(number):
    for i in range(number, 1, -1):
        for j in range(i, 0, -1):
            if i % j != 0 or j == 1:
                farey_list.append(f"{j}/{i}")

    return [farey_list[item] for item in sorted(farey_list.keys())]

print(farey(5))
