#Part 1 
# Stages of Life
Person = 25

if Person < 2:
    print("")


#=============================================================================================
#Hello Admin

#Part 1
User_greetings = ['ADMIN - Ninang',
             'USER - Manny',
             'USER - Ochirrej',
             'USER - Jay',
             'USER - Navi']

User_list = ['admin', 'user1', 'user2', 'user3', 'user4']
ind = 0
for vals in User_list:
    if vals:
        print(f"Welcome {User_greetings[ind]}")
    else:
        print(f"No such user found. Please retry")
    ind += 1

#Part 2

# if User_list:
#     print("Removing all of the user data within the list")
# else:
#     print("We need to find some users")

#Part 3
print("\n=============================================================================== \n")
current_users = ['Manny', 'Ochirrej', 'Navi', 'Ninang', 'Jay']
new_users = ['Ochirrej','Jay','Manny','Gnanin', 'Ivan']

lower_cUsers = []
for reg in current_users:
    lower_cUsers.append(reg.lower())

for users in new_users:
    if users.lower() in lower_cUsers:
        print(f"Username {users} is currently in use. User a different one")
    else:
        print(f"Username {users} is available")

