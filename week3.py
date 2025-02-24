import os
from time import sleep
#pages class page title, button, and displays
class Page:
    def __init__(self, title, content):
        self.title = title
        self.content = {"buttons": content[0], "displays":content[1]}
        
    # display page content
    def display(self):
        print(f"--- {self.title} ---")
        print("Buttons:", self.content["buttons"])
        print("Displays:", self.content["displays"])
        print("------------------\n")



# creates pages
def create_pages():
    landing_page = Page("Landing Page", [["create new list", "load saved list"],["list window",]])
    list_page  = Page("List Page", [["add item", "clear item","save list","main menu"],["list window"]])
    update_list_page = Page("List Page", [["add item", "clear item","save list","main menu"],["list window"]])
    saved_list_page = Page("List Page", [["load list","main menu"],["saved lists window"]])
    return (landing_page, list_page, update_list_page, saved_list_page)

 # Create the pages
def pages():
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



def main_menu():
    """
    Generates:
        clears screen 
        prompts user for input
    Returns:
      int between 0 - 6
    """
    os.system('clear')
    print("Mobile App UX/UI Flow")
    print("1. Pages")
    print("2. Landing Page")
    print("3. Saved List")
    print("4. Update List Page")
    print("5. Saved List Page")
    print("6. Quit")
    try:
        return int(input("Enter choice: "))
    except ValueError:
        return 0

def control_loop():
    while True:
        menu_selection = main_menu()
        if menu_selection == 1:
            pages()
            input("Press enter to continue")
        elif menu_selection == 2:
            landing_page.display()
            input("Press enter to continue") 
        elif menu_selection == 3:
            list_page.display()
            input("Press enter to continue")
        elif menu_selection == 4:
            update_list_page.display()
            input("Press enter to continue")
        elif menu_selection == 5:
            saved_list_page.display()
            input("Press enter to continue")          
        elif menu_selection == 6:
            print("Goodbye")
            exit()
        else:
            print("Invalid selection")
            input("Press enter to continue")

# main entry point
if __name__ == "__main__":
    landing_page = Page("Landing Page", [["create new list", "load saved list"],["list window",]])
    list_page  = Page("List Page", [["add item", "clear item","save list","main menu"],["list window"]])
    update_list_page = Page("List Page", [["add item", "clear item","save list","main menu"],["list window"]])
    saved_list_page = Page("List Page", [["load list","main menu"],["saved lists window"]])
    control_loop()
