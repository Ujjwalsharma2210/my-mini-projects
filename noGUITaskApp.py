###############################################
#                                             #
#       Author UjjwalSharma 19/11/2020        #
#               Version 1.0                   #
#               							  #
###############################################
# Simple kernal based tasks application
# Main list of tasks
listOfTasks = []

# Prints the given list.
def printAllTasks(listOfTasks):
    i = 0
    for task in listOfTasks:
        print("{}. ".format(i) + task)
        i += 1

# deletes the element on the given index.
def deleteTask(listOfTasks, index):
    listOfTasks.pop(index)

def printMenu():
    action = int(input("""Enter 1 to add a task.
Enter 2 to delete a task.
Enter 3 to see your tasks.
Enter 4 to exit.\n"""))
    return action

# Main function.
if __name__ == "__main__":

    userInput = printMenu()
    while userInput != 4:
        if userInput == 1:
            listOfTasks.append(input("Enter your new task: \n"))
        elif userInput == 2:
            printAllTasks(listOfTasks)
            indexToDelete = int(input("Enter the task number you want to delete.\n"))
            deleteTask(listOfTasks, indexToDelete)
        elif userInput == 3:
            printAllTasks(listOfTasks)
        else:
            print("Wrong input, Choose again.")
        userInput = printMenu()
