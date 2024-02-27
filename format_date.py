# https://edabit.com/challenge/co4nwXSvnCjGEu8vp
def format_date(date):
    m,d,y = date.split("/")
    return "".join((y,d,m))

print(format_date("11/12/2019"))
