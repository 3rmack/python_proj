guests = input("Number of quests?\n")
guests = int(guests)
if guests > 50:
    print("Restaurant")
elif 20 <= guests <= 50:
    print("Cafe")
else:
    print("Home")
