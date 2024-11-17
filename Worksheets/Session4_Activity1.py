#Conditional Statements and Loops

# 1
# part A - List of Departments
l_IDDept = [["1","Computer Science"],
           ["2","Mathematics"],
           ["3","Computer Science"],
           ["4","Mathematics"],
           ["5","Physics"],
           ["6","Chemistry"],
           ["7","Biology"],
           ["8","Economics"],
           ["9","Economics"],
           ["10","Psychology"],
           ["11","History"],
           ["12","English"],
           ["13","Philosophy"],
           ["14","Mathematics"],
           ["15","Computer Science"]]

#part B - Loops
WhileLoop_break = 0
forLoop_break = False
id_found = False

while WhileLoop_break == 0:
    print("Enter Course ID to search | quit or 0 to quit.")
    user_input = input("Input search ID: ")
    print("=================================================")

    #part C & D - Conditional statements/Search for department

    #This block of code here is used to look for the user input in the List 
    #If user input is within the list, it returns true
    for row_data in l_IDDept:
        for per_Element in row_data:
                if per_Element == user_input:
                        id_found = True
                        forLoop_break = True  
                        break 
        if forLoop_break:
                break


    if id_found:
            WhileLoop_break = 1
            print(f"Searched ID : {user_input} \n" +
                  f"Department  : {l_IDDept[int(user_input)-1][1]}")
    elif user_input == "0" or user_input == "quit":
            print(f"The value {user_input} has been used to exit")
            WhileLoop_break = 1
    else:
            print(f"Error: Course ID {user_input} is out of range (1-15)")
    
    print("=================================================\n")


