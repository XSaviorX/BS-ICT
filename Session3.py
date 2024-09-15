bicycles = ['trek','cannondale', 'redline', 'specialized']
print("Original list of bicycles: ", bicycles)

print("First bicycle: ", bicycles[0].upper())

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Number of cars in the list: ", len(cars))

bicycles[0] = 'giant'
print("Updated list of bicycles: ", bicycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print("List after appending: ", motorcycles)

motorcycles.insert(0,'harley')
print("List after inserting at index 0: ", motorcycles)

del motorcycles[0]
print("List after using del: ", motorcycles)

# Removing by value using remove()
motorcycles.remove('yamaha')
print("List after removing 'yamaha': ", motorcycles)

# Sorting a list
# Sorting a list permanently using sort()
#=========================================
print("=======================================")
cars.sort()
print("Permanently sorted cars: ", cars)

# Sorting temporarily using sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original list of cars: ", cars)
print("Temporarily sorted cars: ", sorted(cars))
print("Original list after temporary sort: ", cars)
print("=======================================")


print("============== DESCENDING =============")
# Reversing the order of a list
cars.reverse()
print("Reversed list of cars: ", cars)
print("")

orig_num = [7,2,3,5,4]
orig_num.sort()
print("Ascending Order: ", orig_num)
orig_num.reverse()
print("Desceding Order: ", orig_num)
print("=======================================")


#LOOPS
print("================ LOOPS ================")

sum = 0
for num in orig_num :
    sum += num

print("List : ", orig_num)
print("Sum  : ", sum)

print("=======================================\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("=======================================")

print("================ RANGE ================")

range_of_numbers = range(1,5)
for val in range_of_numbers:
    print("Generated value: ", val)

print("=======================================\n")

# Tuples
print("================ Tuples ===============")

dimensions = (200,50)
print("Tuple dimensions", dimensions)

print("=======================================\n")


