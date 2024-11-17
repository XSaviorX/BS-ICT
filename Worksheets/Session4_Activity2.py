#Conditional Statements and Loops

# 2

#Part A and B

#================================================================================
#This variable here is a 3D Lists, and this will hold the Course Information Data
def course_prog():
    Course_Informationn = [
        [["1"],["Introduction to Programming","Computer Science","None"]],
        [["2"],["Calculus I","Mathematics","None"]],
        [["3"],["Data Structures and Algorithms","Computer Science","Introduction to Programming"]],
        [["4"],["Linear Algebra","Mathematics","None"]],
        [["5"],["Physics I","Physics","None"]],
        [["6"],["Chemistry I","Chemistry","None"]],
        [["7"],["Biology I","Biology","None"]],
        [["8"],["Microeconomics","Economics","None"]],
        [["9"],["Macroeconomics","Economics","Microeconomics"]],
        [["10"],["Psychology I","Psychology","None"]],
        [["11"],["History I","History","None"]],
        [["12"],["English Composition I","English","None"]],
        [["13"],["Introduction to Philosophy","Philosophy","None"]],
        [["14"],["Calculus II","Calculus","Calculus I"]],
        [["15"],["Discrete Mathematics","Computer Science","Introduction to Programming"]]
    ]
    #================================================================================

    WhileLoop_break = 0
    forLoop_break = False
    id_found = False

    print("Read first before proceeding")
    print(" - Type in Course ID to search")
    print(" - Type in Quit or 0 to exit ")
    print(" - Course ID input should be within the range of 1-15 \n")

    while WhileLoop_break == 0:
        #Part C
        user_input = input("Search Course ID: ")
        print("=================================================")

        #This block of code here is used to look for the user input in the List 
        #If user input is within the list, it returns true
        for block_data in Course_Informationn:
            for row_data in block_data:
                for per_Element in row_data:
                    if per_Element == user_input:
                        id_found = True
                        forLoop_break = True  
                        break
                    else:
                        id_found = False
                        forLoop_break = False
                if forLoop_break:
                    break
            if forLoop_break:
                break

        #Part D and E
        if id_found:
                print(f"Course ID     : {Course_Informationn[int(user_input)-1][0][0]} \n"
                    f"Course Name   : {Course_Informationn[int(user_input)-1][1][0]} \n"
                    f"Department    : {Course_Informationn[int(user_input)-1][1][1]} \n"
                    f"Prerequisites : {Course_Informationn[int(user_input)-1][1][2]} \n")
                forLoop_break = False
                #WhileLoop_break = 1
        elif user_input == "0" or user_input == "quit":
                print(f"The value {user_input} has been used to exit")
                WhileLoop_break = 1
        else:
                print(f"Error: Course ID {user_input} is out of range (1-15)")
        
        print("=================================================\n")
        