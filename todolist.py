from rich.console import Console

console = Console()

toDoListItems = []


def printListItems():
    if not toDoListItems:
        console.print("List is empty!", style="white bold")
    for item in toDoListItems:
        console.print("\u2022 " + item, style="white bold")


def addListItem():
    console.print("What would you like to add? \n", style="bold #03C9D6")
    itemToAdd = input()
    toDoListItems.append(itemToAdd)
    console.print("Done! Item added to the list!", style="bold #90E314")


def deleteListItem():
    console.print(
        "What would you like to delete? Items currently on the list: \n", style="bold #03C9D6")
    printListItems()
    itemToRemove = input()
    if (not itemToRemove in toDoListItems):
        console.print("Item does not exist!", style="white bold")
        return
    toDoListItems.remove(itemToRemove)
    console.print("Done! Item removed from list!", style="bold #90E314")


while True:
    console.print(
        "What would you like to do? \n", style="bold #03C9D6")
    userChoice = input()
    userChoice.lower()
    match userChoice:
        case "list":
            printListItems()
        case "add":
            addListItem()
        case "delete":
            deleteListItem()
        case "exit":
            console.print("Exiting...", style="white bold")
            break
