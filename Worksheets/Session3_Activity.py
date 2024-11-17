print("================ LISTS ================")

#Lists Basic
#1.1
units = ['Introduction to Programming','Calculus I','Data Structures and Algorithms', 
         'Linear Algebra', 'Physics I', 'Chemistry I', 'Biology I', 'Macroeconomics', 
         'Psychology I', 'History I', 'English Composition I', 'Introduction to Philosophy', 
         'Calculus II', 'Discrete Mathematics']
#used for 3
new_units = ['Introduction to Programming','Calculus I','Data Structures and Algorithms', 
         'Linear Algebra', 'Physics I', 'Chemistry I', 'Biology I', 'Macroeconomics', 
         'Psychology I', 'History I', 'English Composition I', 'Introduction to Philosophy', 
         'Calculus II', 'Discrete Mathematics']
#used for 4
a_courses = ['Introduction to Programming','Calculus I','Data Structures and Algorithms', 
         'Linear Algebra', 'Physics I', 'Chemistry I', 'Biology I', 'Macroeconomics', 
         'Psychology I', 'History I', 'English Composition I', 'Introduction to Philosophy', 
         'Calculus II', 'Discrete Mathematics']

#1.2
print(f"#1.2 - List of Units: \n{units}\n")

#Lists Sorted()
#2.1
sorted_units = sorted(units)
#2.2
print(f"#2.2 - Sorted List: \n{sorted_units}\n")
#2.3
reverse_units = sorted(units,reverse=True)
print(f"#2.4 - Reverse List: \n{reverse_units}\n")

#Lists Reverse()
#3.1
units.reverse()
#3.2
print(f"#3.2 - Reverse List: \n{units}\n")
#3.3
changed_UnitOrder = units
changed_UnitOrder.reverse()
#3.4
print(f"#3.4 - Changed Unit Order List: \n{changed_UnitOrder}\n")

#Lists Sort()
#4.1
units.sort()
#4.2
print(f"#4.2 - Alphabetical Ordered List: \n{units}\n")
#4.3
units.sort(reverse=True)
#4.4
print(f"#4.4 - Reversed Alphabetical Ordered List: \n{units}\n")

print("=======================================\n")

#Part 2
print("Part 2")
#1
orig_units = units
orig_units.sort()
n_units = new_units
n_units.sort()
num = 1
ind = 0
print(f"The following courses are available for expression of interest if the students meet the prerequisites \n")
for val in n_units:
    print(f"{num} - {val}")
    num += 1

#2
num = 1
n_units[0] = "Database I"

print(f"\n======== ORIGINAL LIST =============== UPDATED LIST ========")
indent = 34
for n_lists in orig_units:
    if num < 10:
        indent += 1

    print(f"{num} ", n_lists.ljust(indent), end=f"- {n_units[ind]} \n")
    num += 1
    ind += 1
    indent = 34

print(f"\nWithdrawn Course: {orig_units[0]}")
print(f"New Course :\t  {n_units[0]}")

print("\n================== AVAILABLE COURSES ========================\n")
num = 1
a_course = a_courses
#3.2
a_course.insert(0,n_units[0])
#3.3
mid = len(a_course)//2
a_course.insert(mid,"Intro to Elgoog")
#3.4
a_course.append("Intro to Big Data")

for val in a_course:
    print(f"{num} - {val}")
    num += 1

print("\n=============== IMPORTANT ANNOUNCEMENT =====================\n")

u_units = []
num = 1
ind = 0
new_list = []
for indx in range(4):
    tempVar = a_course.pop()
    u_units.append(tempVar)
    new_list = a_course


print("There are some changes for the availability of the courses \n" +
      "offered this semester, Please double check on the following list\n")
print("Possible Reasons: Room Availability or Technical/Course Inssues\n")

print(f"==== AVAILABLE COURSES ============== UNAVAILABLE COURSES =====")

for subs in new_list:
    if ind < len(u_units):
        print(f"{num} ", subs.ljust(indent), end=f"- {u_units[ind]} \n")
    else:
        print(f"{num} ", subs.ljust(indent), end=f"\n")
        
    num += 1
    ind += 1

print("=============================================================\n")

#TUPLES and LOOPS
#part I
t_units = (("1","Introduction to Programming"),
           ("2","Calculus I"),
           ("3","Data Structures and Algorithms"),
           ("4","Linear Algebra"),
           ("5","Physics I"),
           ("6","Chemistry I"),
           ("7","Biology I"),
           ("8","Microeconomics"),
           ("9","Macroeconomics"),
           ("10","Psychology I"),
           ("11","History I"),
           ("12","English Composition I"),
           ("13","Introduction to Philosophy"),
           ("14","Calculus II"),
           ("15","Discrete Mathematics"))

list_IDNames = []
#part II
for t_val in t_units:
    print(f"This is the extracted course name ({t_val[1]}) and now storing it to the empty list")
    list_IDNames.append(t_val[1]) 
    #looping through each tuples using the indexes to get the desired value 
    #and store it to the variable list_IDNames
    
#part III
print("\nList of Course Information")
num = 1
# This loop here is just used for printing the value of list_IDNames which holds the extracted Course Names from the tuple
for vals in list_IDNames:
    print(f"{num}. {vals}")
    num += 1


print("\n=============================================================================== \n")