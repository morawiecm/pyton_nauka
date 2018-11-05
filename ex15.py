from sys import argv

script, filename = argv

txt = open(filename)

print(f"Oto twoj plik {filename}:")
print(txt.read())

print("Wpisz ponownie nazwe pliku:")
file_again = input('> ')

txt_again = open(file_again)
print(txt_again.read())
