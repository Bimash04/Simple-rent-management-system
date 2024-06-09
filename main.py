import displayMenu
import operation

instruction = displayMenu.displayMenu()

if (instruction == 1):
    operation.operation(False)
elif (instruction == 2):
    operation.operation(True)
else:
    print("Program Exited!")
