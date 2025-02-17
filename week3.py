import os
from time import sleep

class Page:
    def __init__(self, title, content):
        self.title = title
        self.content = {"buttons": content[0], "displays":content[1]}
        

    def display(self):
        print(f"--- {self.title} ---")
        print("Buttons:", self.content["buttons"])
        print("Displays:", self.content["displays"])
        print("------------------\n")




def create_pages():
    landing_page = Page("Landing Page", [["create new list", "load saved list"],["list window",]])
    list_page  = Page("List Page", [["add item", "clear item","save list","main menu"],["list window"]])
    update_list_page = Page("List Page", [["add item", "clear item","save list","main menu"],["list window"]])
    saved_list_page = Page("List Page", [["load list","main menu"],["saved lists window"]])
    return (landing_page, list_page, update_list_page, saved_list_page)


def pages():
    # Create the pages
    landing_page = Page("Landing Page", [["create new list", "load saved list"], ["list window"]])
    list_page  = Page("List Page", [["add item", "clear item", "save list", "main menu"], ["list window"]])
    update_list_page = Page("Update List Page", [["add item", "clear item", "save list", "main menu"], ["list window"]])
    saved_list_page = Page("Saved List Page", [["load list", "main menu"], ["saved lists window"]])
    
    print("=== Application Page Flow ===\n")
    
    # Start at the Landing Page
    print("1. Landing Page:")
    landing_page.display()
    
    # User selects "create new list" to go to the List Page
    print("-> User selects 'create new list'\n")
    print("2. List Page:")
    list_page.display()
    
    # From the List Page, the user adds an item
    print("-> User selects 'add item'\n")
    print("3. Update List Page:")
    update_list_page.display()
    
    # After updating, the user saves the list
    print("-> User selects 'save list'\n")
    print("4. Saved List Page:")
    saved_list_page.display()
    
    # Finally, the user returns to the main menu (landing page)
    print("-> User selects 'main menu'\n")
    print("5. Landing Page (Return):")
    landing_page.display()

# takes users input prints UML object and returns to menu
def menu_clean_up():
        input("press any key to continue")
        menu()


# handles menu controlflow
def menu():
    os.system('clear')
    menu_message = f"""Anschutz Modifed Waterfall
    1 - Pages
    2 - Landing Page
    3 - List Page
    4 - Update List Page
    5 - Saved List Page
    q - Quit
    """
    print(menu_message)
    selection = input("Select Menu Item: ").lower()
    if selection == "1":
         pages()
         menu_clean_up()
    elif selection == "2":
       landing_page.display()
       menu_clean_up()
    elif selection == "3":  
        list_page.display()
        menu_clean_up()
    elif selection == "4": 
        update_list_page.display()
        menu_clean_up()
    elif selection == "5":
        saved_list_page.display()
        menu_clean_up()
    elif selection == "q":
        print("Have a great day!")
        exit
    else:
        print("invalid selection enter 1,2,3,4,5,6,7,8 or q")
        sleep(10)
        menu()

# main entry point
if __name__ == "__main__":
    landing_page = Page("Landing Page", [["create new list", "load saved list"],["list window",]])
    list_page  = Page("List Page", [["add item", "clear item","save list","main menu"],["list window"]])
    update_list_page = Page("List Page", [["add item", "clear item","save list","main menu"],["list window"]])
    saved_list_page = Page("List Page", [["load list","main menu"],["saved lists window"]])
    menu()
