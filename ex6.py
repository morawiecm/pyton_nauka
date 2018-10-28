types_of_people = 10
x = f"Istnieje {types_of_people} rodzajow ludzi"

binary = "binarny"
do_not = "nie znaja"
y = f"Ci, ktorzy znaja system {binary} i ci, kotrzy go {do_not}"

print(x)
print(y)

print(f"Powiedzialem: {x}")
print(f"Powiedzialem rowniez: '{y}'")

hilarious = False
joke_evaluation = "Czyz to nie jest przezabawny dowcip? {}"

print(joke_evaluation.format(hilarious))

w = "To jest lewa strona..."
e = "łancucha zankow z prawa strona"

print(w + e)
