def add(a, b):
    print(f"DODAWANIE {a}+{b}")
    return a + b


def substract(a, b):
    print(f"ODEJMOWANIE {a}-{b}")
    return a - b


def multiply(a, b):
    print(f"MNOZENIE {a}*{b}")
    return a * b


def divide(a, b):
    print(f"DZIELENIE {a}/{b}")
    return a / b


print("Wykonajmy kilka operacji arytmetycznych jednie za pomoca napisanych funkcji")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Wiek: {age}, wzrost: {height}, waga: {weight}, IQ: {iq}")

# to lamiglowka za dodatkowe punkty ale i tak ja wpisz

print("Oto zadanie: ")
what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("To daje", what, " czy dalbys rade obliczyc to recznie ?")
