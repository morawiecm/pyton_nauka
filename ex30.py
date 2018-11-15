people = 30
cars = 40
trucks = 15

if cars > people:
    print("Powinnismy jechac samochodami.")
elif cars < people:
    print("Nie Powinnismy jechac samochodami")
else:
    print("Nie mozemy sie zdecydowac")

if trucks > cars:
    print("Jest zbyt duzo ciezarowek")
elif trucks < cars:
    print("Moze Powinnismy wziac ciezarowki")
else:
    print("Nadal nie mozemy sie zdecydowac")

if people > trucks:
    print("W porzadku, po prostu wezmy ciezarowki")
else:
    print("Dobra, w takim razie zostajemy w domu")
