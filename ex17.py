from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Kopiowanie z {from_file} do {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"Plik wejsciowy{len(indata)} bajtow")

print(f"Czy plik wyjsciowy istnieje? {exists(to_file)}")
print("Nacisnij RETURN zeby kontynuowac lub CTRL+C, zeby anulowac")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("w porzadku zrobione.")

out_file.close()
in_file.close()
