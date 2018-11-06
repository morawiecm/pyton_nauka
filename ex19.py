def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"Masz {cheese_count} kawalkow sera!")
    print(f"Masz {boxes_of_crackers} paczek krakersow")
    print("Stary wystaczy zrobic impreze")
    print("Zorganizuj sobie koc\n")


print("Mozemy po porostu bezposrednio podac funkcji liczby:",
      cheese_and_crackers(20, 30))

print("Albo mozemy uzyc zmiennych ze skrpty:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Mozemy rowniez wykonac wewnatrz operacje arytmetyczne:")
cheese_and_crackers(10 + 20, 5 + 6)

print("I mozemy polaczyc te dwie rzeczy, czyli zmienne i operacje arytmetyczne:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
