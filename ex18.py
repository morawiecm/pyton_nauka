# ta funkcja jest podoba do skryptkow z argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1},arg2: {arg2}")

# ok, to *args jest wlasciwie bezcelowe; mozemy po prostu zrobic tak


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1},arg2: {arg2}")

# ta funkcja przyjmuje po porstu jeden argument


def print_one(arg1):
    print(f"arg1: {arg1}")

# ta funkcja nie przyjmuje zadnych argumentow


def print_none():
    print("Ja nic nie mam")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("Pierwszy!")
print_none()
