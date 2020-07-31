# groceries = {
# "baby spinach": 2.78,
# "hot chocolate": 3.70,
# "crackers": 2.10,
# "bacon": 4.50,
# "carroets": 6.70,
# "oranges": 6.90
# }

# # print(groceries)

# # print(groceries["bacon"])

# # groceries["avos"] = 1.00
# # print (groceries)

# for item in groceries:
#     print(item, groceries[item])

# print()

# for item, price in groceries.items():
#     print(item, price)


cohorts = {
    "perth": ["anna", "katie", "elsa"],
    "brisbane": ["teagan", "vivi", "nic"]
}

print(cohorts["perth"])


# for cohort, peeps in cohorts.item():
#     print(f"{cohorts} {peeps})
#     for peep in peeps:
#         print(f"       {peep}")


all_cohorts = {
    2019: {
        "perth": ["Anna", "Sarah", "Nina", "Ellie"]
    },
    2020: {
        "perth": ["Anna", "Viv", "Nic", "Teagen"],
        "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
    }
}


for year, cohorts in all_cohorts.items():
    print(year)
    for city, cohort in cohorts.items():
        print(f"  {city}")
        for peep in cohort:
            print("    {peep}")










# Q1) ​Once again we are going to work on our grocery receipt. This time, however, use the following dictionary to define the items and their prices:

groceries = {
      "Baby Spinach": 2.78,
      "Hot Chocolate": 3.70,
      "Crackers": 2.10,
      "Bacon": 9.00,
      "Carrots": 0.56,
      "Oranges": 3.08
}

print(groceries)

# can look up the value of the key by using the name
print(groceries["Bacon"])

# can add ot the list by using the name or update the values ie change from 1.00 to 2.00
# groceries["Avocadoes"] = 1.00

print(groceries)





#solution- not fininshed


# total_cost = 0
# quantities = []

# for item, price in groceries.items():
#     quantity = input(f"What quantity of {item} you like? ")
#     quantities.append(int(quantity))
#     new_price = float(price) * int(quantity)
#     total_cost += float(new_price)
#     price = groceries[item]
#     groceries[item] = [price, new_price]

# print()
# print(quantities)
# print()
# total_cost = f"${total_cost:.2f}"
# print(total_cost)


# print()
# print("====Izzy's Food Emporium====")
# for item, groceries in groceries.items():
#     print(f"{item:<18} ${groceries['price']:.2f}")
# print("============================")
# print(f"                   {total_cost}")







# Q2) Given the list of names below, create a dictionary where each key is a name and the value is the number of
# times that name occurs in the list.




# 1. Read in the list of names
my_dict = {
    "key": "value"
}

names = [
"Maddy", "Bel", "Elnaz", "Gia", "Izzy",
"Joy", "Katie", "Maddie", "Tash", "Nic",
"Rachael", "Bec", "Bec", "Tabitha", "Teagen",
"Viv", "Anna", "Catherine", "Catherine", "Debby",
"Gab", "Megan", "Michelle", "Nic", "Roxy",
"Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

# 2. For each name
for name in names:
    print(name)

# 3. If I haven't see the name before, add it to a dictionary and set it's value to 0, otherwise increment it's value by 1.
   


    if name in my_dict.keys():
        my_dict ["key"] += 1
    else:
        my_dict[name] = 1


# 4. Output the resulting dictionary.

for key, value in my_dict.items():
    print(key,value)

    print (str(my_dict))
