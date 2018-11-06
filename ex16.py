from sys import argv

script, filename = argv

print(f"Wymazemy {filename}")
print("Jeśli tego nie chcesz, wcisnij CTRL+C (^C).")
print("Jeśli tego chcesz, wcisnij RETURN.")

input("?")

print("Otwieranie pliku....")
target = open(filename, 'w')

print("Wykasowywanie pliku. Do widzenia...")
target.truncate()

print("Teraz poprosze Cię o wpisanie trzech lini tekstu")

line1 = input("linia 1: ")
line2 = input("linia 2: ")
line3 = input("linia 3: ")

print("Zapisze je w pliku")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("A na koniec zamykamy plik")
target.close()

print(f"I wyswietlimy to co zostalo wpisane do pliku: {filename}")
target = open(filename)
print(target.read())
