def displayMenu():
#    global bestClass
    print("""
1: Option 1
2: Option 2
3: Option 3
0: Quit""")
    bestClass = "Year 11 CS"
    print("subRoutine. bestClass currently holds:",bestClass)
#end displayMenu
 
print("Welcome to my subroutine example")
bestClass = "Year 10 CS"
print("Main 1. bestClass currently holds:",bestClass)
print("The program is running the procedure displayMenu: ")
displayMenu()
print("Main 2. bestClass currently holds:",bestClass)
input("The program has finished running the procedure displayMenu: ")
 
"""userChoice = """
while userChoice not in ["0","1","2","3"]:
    print("Please select an option 0-3")
    userChoice = input()
#endwhile