print(""" Wchodzisz do ciemnego pokoju z dwoma drzwiami,
przechodzisz przez drzwi na 1 czy nr 2? """)

door = input("> ")

if door == "1":
    print("Widzisiz tam wielkiego niedziwiedzia, ktory zjada sernik.")
    print("Co robisz?")
    print("1. Zabierasz sernik.")
    print("2. Krzyczysz na niedziwiedzia")

    bear = input("> ")

    if bear == "1":
        print("Niedzwiedz odgryza ci nos. Dobra robota!")
    elif bear == "2":
        print("Niedzwiedz odgryza ci nogi. Dobra robota!")
    else:
        print(f"Coz, {bear} to prawdopodnie najlepszy wybor")
        print("Niedzwiedz ucieka")
elif door == "2":
    print("Wpatrujesz sie w nieskonczona otchlan oka Cthulhu")
    print("1.Jagody")
    print("2.Zolte spinacze do bielizny")
    print("3.Wyrozumiale reolwey nuca melodie")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Twoje cialo ocalalo ale mozg masz jak galaretka owocowa")
        print("Dobra robota")
    else:
        print("Z szalenstwa gnija ci oczy i zamieniaja sie w kaluze blota")
        print("Dobra robota")
else:
    print("Potykasz sie, nadziewasz sie na noz i umierasz. Dobra robota")
