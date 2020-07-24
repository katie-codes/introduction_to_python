

#q1

# counter = 0
# number_list = []

# while counter < 4:
#     number = int(input("Enter a number: "))
#     number_list.append(number)
#     counter = counter + 1
# total = sum(number_list)
# print(total)





# q2

# mailing_list = [
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Biscuit", "biscuit@whippies.park"],
# ["Rory", "rory@whippies.park"],
# ]


# for send in mailing_list:
#     print (f"{send[0]}: {send[1]}")






#q3

# names = []

# name_1 = str(input("What's your name:"))
# name_2 = str(input("What's your name:"))
# name_3 = str(input("What's your name:"))

# names.append(name_1)
# names.append(name_2)
# names.append(name_3)

# print(names)



#q4

# groceries = [
#       ["Baby Spinach", 2.78],
#       ["Hot Chocolate", 3.70],
#       ["Crackers", 2.10],
#       ["Bacon", 9.00],
#       ["Carrots", 0.56],
#       ["Oranges", 3.08]
# ]



# item_spinach = str(input("How much Baby Spinach did you buy?"))
# item_hot_choc = str(input("How much Hot Chocolates did you buy?"))
# item_crackers = str(input("How many Crackers did you buy?"))
# item_bacon = str(input("How much Bacon did you buy?"))
# item_carrots = str(input("How many Carrots did you buy?"))
# item_oranges = str(input("How many Oranges did you buy?"))


# for item in groceries:
#     # print(f"{item[0]} (${item[1]} * {item_spinach})")
#     print (f"{item[1] * {item_spinach}}")


# copied from slack to break down and see how it works
# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]
# total = 0
# for item in groceries:
#     quantity = input(f"What quantity of {item[0]} would you like? ")
#     item[1] = item[1] * int(quantity)
#     total += item[1]
# total = f"${total:.2f}"
# print("====Izzy's Food Emporium====")
# for item in groceries:
#     print(f"{item[0]:<20} ${item[1]:.2f}")
# print("============================")
# print(f"{total:>27}")



groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

total = 0

for item in groceries:
    quantity = input(f"What quantity of {item[0]} would you like? ")
    item[1] = item[1] * int(quantity)
    total += item[1]

print("====Izzy's Food Emporium====")
for item in groceries:
    print(f"{item[0]:<20} ${item[1]:.2f}")
print("============================")
print(f"${total:.2f}")

