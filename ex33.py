i = 0
numbers = []

while i < 6:
    print(f"Na gorze i ma wartosc {i}")
    numbers.append(i)

    i += 1

    print("Aktualne liczby to: ", numbers)
    print(f"Na dole i ma wartosc {i}")

    print("Te liczby to:")

    for num in numbers:
        print(num)
