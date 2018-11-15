the_count = [1, 2, 3, 4, 5]
fruits = ['jablka', 'pomarancze', 'gruszki', 'morele']
change = [1, 'jednogroszowki', 2, 'dwugroszowki', 3, 'trzypieciogroszowki']

# to jest pierwszy rodzaj petli for kotra przechodzi przez liste
for number in the_count:
    print(f"To jest liczba {number}")

# to samo co wyzej
for fruit in fruits:
    print(f"Rodzaj owocu {fruit}")

# mozemy rowniez przechodzic przez listy mieszane
# zwroc uwafe, ze musimy uzyc {}, poniewaz nie iemy co wniej jest

for i in change:
    print(f"Mam {i}")

# mozemy tez budowac listy, zaczniemy od pustej

elements = []

# nastepnie uzywamy funkcji range, aby odliczyc od 0 do 5

for i in range(0, 5):
    print(f"Dodajemy {i} do konca tej listy.")
    # append jest funkcja ktora listy rozumieja
    elements.append(i)

# teraz mozemy je rowniez wydrukowac

for i in elements:
    print(f"Tym elementem bylo {i}")
