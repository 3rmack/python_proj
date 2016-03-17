# import collections
# Sale = collections.namedtuple("Sale", "productid customerid date quantity price")
# sales = []
# sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
# sales.append(Sale(419, 874, "2008-09-15", 1, 18.49))
# #print(sales)
# #print(sales[0].price)
# total = 0
# for sale in sales:
#     total += sale.quantity * sale.price
# print("Total ${0:.3f}".format(total))  # выведет: Total $42.46

# Aircraft = collections.namedtuple("Aircraft", "manufacturer model seating")
# Seating = collections.namedtuple("Seating", "minimum maximum")
# aircraft = Aircraft("Airbus", "A320-200", Seating(100, 220))
# print(aircraft.manufacturer)

# L = [3, 56, 7, 11, 6]
# def func (a, b, c, d, e):
#     return(a*b*c*d*e)
# print(func(*L))


leaps = [y for y in range(1900, 1940)]
print(leaps)
leaps = [y for y in range(1900, 1940) if y % 4 == 0]
print(leaps)
leaps = [y for y in range(1900, 1940) if (y
                                          % 4 == 0 and y % 100 != 0) or (y % 400 ==0)]
print(leaps)

codes = []
for sex in "MF":  # мужская (Male), женская (Female)
    for size in "SMLX":  # маленький, средний, большой, очень большой
        if sex == "F" and size == "X":
            continue
        for color in "BGW":  # черный (Black), серый (Gray), белый (White)
            codes.append(sex + size + color)
print(codes)

codes = [s + z + с for s in "MF" for z in "SMLX" for с in "BGW" if not (s == "F" and z == "X")]
print(codes)
