is_raining = True
if is_raining:
    print("You'll need an umbrella today.")
temperature = 21
if temperature <= 16:
    print("Take a jumper today.")
else: 
    print("no need for a jumper today")
    
temperature = 17
is_cold = temperature < 16
is_hot = temperature > 25

print(is_cold, is_hot)
if is_cold:
    print("Take a jumper today.")
elif is_hot:
    print("Yuck, stay at home.")
else:
    print("Have a great day!")