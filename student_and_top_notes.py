# https://edabit.com/challenge/5KqHNS9wS97zN7Xyy

def top_note(dict):
    [student, notes] = dict.values()
    return student, max(notes)

print(top_note({ "name": "John", "notes": [3, 5, 4] }))