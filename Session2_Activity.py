#====== 1 =======
a = 15
b = 12

print(type(a))
print(type(b))
#


#======= 2 =======
print(f'a + b = {a + b}') # addition
print(f'a - b = {a - b}') # subtraction
print(f'a * b = {a * b}') # multiplication
print(f'a / b = {a / b}') # division
#

#======= 3 =======
c = int(a / b)
print(f'Value of c = {c} \nType of c  = {type(c)}')

c = float(a/b)
print(f'Value of c = {c} \nType of c  = {type(c)}')

#

#======= 4 ======
message = "The result of a divided by b is"
c_message = message + str(c)
print(c_message)
# 

#====== 5 =======
res1 = a > b
res2 = a == b
print(res1)
print(res2)
#
