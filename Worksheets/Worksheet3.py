
import pandas as pd
import sys

#Working with Dictionaries

#-----------------------------------------------------------
#Declaration and Initialization of variables for part 1
indent = 20

def session5_part1():
    #1 Student Course Enrollment
    course_enrollments = {
        '1001' : ['CS101','MATH101'],
        '1002' : ['CS101','MATH102'],
        '1003' : ['CS202','PHY101'],
        '1004' : ['CS202','CHEM101'],
        '1005' : ['BIO101','HIST101'],
        '1006' : ['BIO102','ENGL101'],
        '1007' : ['ECON101','PSY101'],
        '1008' : ['ECON102','SOC101'],
        '1009' : ['PSY102','SOC102'],
        '1010' : ['CS101','MATH101'] 
    }
    #Printing list for Student and their respective class schedules
    print("Student                   Course Codes")
    for student_items in course_enrollments:
            print(f"{student_items.ljust(indent+6)} {', '.join(map(str,course_enrollments[student_items]))}\n")


def session5_part2():
    #2 Class schedule
    departments = {
        'Computer Science': (('Computer Science','CS101','Introduction to Computer Science'),
                            ('Computer Science','CS202','Data Structures and Algorithms')),
        'Mathematics': (('Mathematics','MATH101','Calculus I'),
                        ('Mathematics','MATH102','Calculus II')),
        'Physics': (('Physics','PHY101','General Physics I'),
                    ('Physics','PHY102','General Physics II')),
        'Chemistry': (('Chemistry','CHEM101','General Chemistry I'),
                    ('Chemistry','CHEM102','General Chemistry II')),
        'Biology': (('Biology','BIO101','Biology I'),
                    ('Biology','BIO102','Biology II')),
        'History': (('History','BIO101','Biology I'),
                    ('History','BIO102','Biology II')),
        'English': (('English','ENGL101','English Composition I'),
                    ('English','ENGL102','English Composition II')),
        'Economics': (('Economics','ECON101','Principles of Economics'),
                    ('Economics','ECON102','Intermediate Microeconomics')),
        'Psychology': (('Psychology','PSY101','Introduction to Psychology'),
                    ('Psychology','PSY102','Developmental Psychology')),
        'Sociology': (('Sociology','SOC101','Introduction to Sociology'),
                    ('Sociology','SOC102','Social Problems')),
        }

    #==================== Output/Printout for Part 1 ================================
    #2
    #printing the class schedule
    print("Department           Course ID       Course Name")
    for dept in departments:
            print(f"{dept.ljust(indent)} {departments[dept][0][1].ljust(15)} {departments[dept][0][2]}")
            print(f"{dept.ljust(indent)} {departments[dept][1][1].ljust(15)} {departments[dept][1][2]}\n")

    print('=======================================================================================================')

def session5_part3():
    #3. Lecturer Assignments
    lecturer_assignments = {
            #'Dr. John Doe' : (),#1
            #'Prof. Jane Smith' : (),#2
            'Mr. Michael Johnson' : ['CS202','PHY102'],#3
            'Dr. Emily Brown' : ['CS101','MATH102'],#4
            'Prof. David Lee' : ['PHY101'],#5
            'Asst. Prof. Olivia Taylor' : ['MATH101','CHEM101'],#6
            #'Dr. Noah Wilson' : (),#7
            'Miss. Sophia Carter' : ['CHEM102','BIO101','BIO102'],#8
            #'Asst. Prof. Jacob Miller' : (),#9
            #'Dr. Emma Davis' : (),#10
            #'Mrs. Ethan Jones' : (),#11
            #'Asst. Prof. Ava Martinez' : (),#12
            'Dr. Oliver Hernandez' : ['HIST101','HIST102','ENGL101'],#13
            'Prof. Isabella Garcia' : ['ENGL102','SOC101'],#14
            'Asst. Prof. Liam Lopez' : ['SOC102'],#15
            #'Dr. Mia Gonzalez' : (),#16
            #'Prof. Elijah Rodriguez' : (),#17
            #'Asst. Prof. Amelia Perez' : (),#18
            'Dr. Lucas Sanchez' : ['PSY101','PSY102'],#19
            'Prof. Evelyn Russell' : ['ECON101','ECON102']#20
    }
    #-----------------------------------------------------------

    #3
    #Printing list for leturers and their respective class schedules
    print("Lecturer                   Course Codes")
    for lect_items in lecturer_assignments:
            print(f"{lect_items.ljust(indent+6)} {', '.join(map(str,lecturer_assignments[lect_items]))}\n")

    print('=======================================================================================================')



#==========Working with User inputs and While Loops=======================

#-------------------------------------------
#Declaration and Initialization of variables for part 2

#List, Dictionaries and Tuples
student_list = []
location = {}

#String
room_number = ""
room_capacity = ""
room_floorNumber = ""
room_location = ""

#Numeric 
capacity = 0

#csv files
csv_location = pd.read_csv('csv_files\Location.csv', header=0)

for index, row in csv_location.iterrows():

    room_number = row.iloc[0]
    room_capacity = row.iloc[1]
    room_floorNumber = row.iloc[2]
    room_location = row.iloc[3]

    #if true then add new items to the dictionary location
    if room_number not in location:
        #first add the key
        location[room_number] = {}
        #then add the values using the key
        location[room_number] = [
              room_capacity, 
              room_floorNumber,
              room_location
        ]     


#-------------------------------------------

#==================== Output/Printout for Part 2 ================================

def session6_part1():
    student_lists = []
    count = 1
    while True:
        u_name = input("Enter Username: ")
        if u_name == "admin":
            print("------------Creating Class list--------------")
            print(" - Type in quit, exit or 0 to exit")
            while True:
                student_name = input("Enter Student Name: ")

                if student_name in ['quit','0','exit']:
                        break
                else:
                    student_lists.append(student_name)
            
            print("Printing Final Class List")
            for s_names in student_lists:
                print(f"{count} {s_names}")
                count +=1
            
            count = 0
            break
        else:
            print("Username not accepted")

def session6_part2():
    capacity = input('Please input room capacity: ')
    if capacity == 0:
        print("ERROR: Capacity can not be 0. \nRoom Capacity minimum is 10, maximum is 40 \n Please re-run the program")
    else:

        for key, limit in location.items():
            if int(capacity) < limit[0]:
                room_number = key
                room_capacity = limit[0]
                room_floorNumber = limit[1]
                room_location = limit[2]
                break

        
        print(f'Room Information')
        print(f"Number: {room_number}")
        print(f"Capacity: {room_capacity}")
        print(f"Floor Number: {room_floorNumber}")
        print(f"Location: {room_location}")
    

def session6_part3():
    print('============ INSTRUCTIONS ================\n')
    print(' - Input the number of students in the class')
    print(' - Room Capacity or Number of Students can not be 0')
    print(' - Room Capacity minimum is 10, maximum is 40')
    print(' - Input the the names of the students')
    print(' - Input quit, exit or 0 to stop')
    print('\n==========================================\n')

    #Locate rooms that can support the number of users
    capacity = input('Please input room capacity: ')
    if capacity == 0:
        print("ERROR: Capacity can not be 0. \n Please re-run the program")
    else:

        for key, limit in location.items():
            if int(capacity) < limit[0]:
                room_number = key
                room_capacity = limit[0]
                room_floorNumber = limit[1]
                room_location = limit[2]
                break

        
        print(f'Room Information')
        print(f"Number: {room_number}")
        print(f"Capacity: {room_capacity}")
        print(f"Floor Number: {room_floorNumber}")
        print(f"Location: {room_location}")

        #Username / Student Name input loop
        print("\nCreating a Student List")
        n_capacity = int(capacity)
        while n_capacity >0:
            student_name = input("Please input student name: \n")
            #Exit program loop
            if student_name in ['quit','0','exit']:
                 break
            else:
                student_list.append(student_name)
                print('Student have been added to the class')
            
            n_capacity -= 1


        student_count = 1
        print('Final Result for class')
        print('-----Student List-----')
        for s_list in student_list:
            print(f'{student_count} - {s_list}')
            student_count+=1

        print(f'Room Information')
        print(f"Number: {room_number}")
        print(f"Student Number: {student_count - 1}")
        print(f"Capacity: {room_capacity}")
        print(f"Floor Number: {room_floorNumber}")
        print(f"Location: {room_location}")

    print('\n==========================================\n')


def session6_part4():
    count = 1
    l_count = 1
    input_list = []
    try:
        while True:
            
            u_input = input(f"Input #{count}: ")
            print(f"- {u_input}")

            input_list.append(u_input)
            # for items in input_list:
            #     print(f"{l_count} - {items}")
            #     l_count += 1

            print(f"Total number of inputs: {len(input_list)}")
            #l_count = 1
            count += 1
    except KeyboardInterrupt:
        print(f"\n\n---------------------------\n Program has stopped. \n ---------------------------")
        sys.exit()


#Menu selection variables
loop_break = True
selected_opt = ""

#Menu Selection

while loop_break:
     print(f"Please select one of the choices")
     print(f"Press A for Session 5 Part 1")
     print(f"Press B for Session 5 Part 2")
     print(f"Press C for Session 5 Part 3")
     print(f"-----------------------------")
     print(f"Press D for Session 6 Part 1")
     print(f"Press E for Session 6 Part 2")
     print(f"Press F for Session 6 Part 3")
     print(f"Press G for Session 6 Part 4")

     selected_opt = input("Input Selection: ")

     if selected_opt == "A":
          session5_part1()
     elif selected_opt == "B":
          session5_part2()
     elif selected_opt == "C":
          session5_part3()
     elif selected_opt == "D":
          session6_part1()
     elif selected_opt == "E":
          session6_part2()
     elif selected_opt == "F":
          session6_part3()
     elif selected_opt == "G":
          session6_part4()
