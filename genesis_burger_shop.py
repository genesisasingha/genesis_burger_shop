print("GENESIS BURGER SHOP")
burger_size = input("what is your burger size? s, m, l: ")
add_fries = input("do you want to add fries? y/n: ")
add_drink = input("do you want to add a drink? y/n: ")
bill = 0
if burger_size == "s":
    bill += 10
elif burger_size == "m":
    bill +=15
elif burger_size == "l":
    bill += 20
else:
    print("invalid size")
if add_fries == "y":
    if burger_size == "s":
        bill += 2
    elif burger_size == "m":
       bill += 3
    elif burger_size == "l":
        bill += 4
elif add_fries == "n":
    pass
else:
    print("invalid option")
if add_drink == "y":
            bill += 1
elif add_drink == "n":
 pass
else:
    print("invalid option")
print(f"your total bill is ${bill}")   
