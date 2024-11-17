number = 5
if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")

toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in toppings:
    print("Adding mushrooms")

if 'extra cheese' in toppings:
    print("Adding extra cheese")

x = 10

if x := 3:
    print(x)
else:
    print(x)

a_toppings = ['mushrooms', 'olives', 'green pepper']
r_toppings = ['mushrooms', 'french fries']

for topping in r_toppings:
    if topping in a_toppings:
        print(f"Adding {topping}")
else:
    print(f"Sorry, we don't have {topping}")