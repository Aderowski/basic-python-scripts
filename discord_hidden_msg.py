import pyperclip as cb
def convert_to_hidden(msg):
    return "".join([f"|| {l} ||" for l in msg])

msg = str(input())
cb.copy(convert_to_hidden(msg))