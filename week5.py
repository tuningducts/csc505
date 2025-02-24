import os
def make_bold(text):
    """
     Helper function
     Generates
        bold and green text
     Returns
        text
    """
    return "\033[1;32m" + text + "\033[0m"

class Actor:
    """
    Represents an actor in a use case diagram.
    Attributes:
        name (str): The name of the actor.
        use_cases (list[str]): A list of use cases associated with the actor.
    Methods:
        display():
            Prints the actor's name and their associated use cases.
    """
    def __init__(self, name:str, use_cases:list[str]):
        self.name = name
        self.use_cases = use_cases
    
    def display(self):
        print(f"{make_bold('Actor')}: {self.name}")
        print("-----------------")
        for use_case in self.use_cases:
            use_case.display()


class Use_Case:
    """
    A class to represent a use case in a system.
    Attributes
    ----------
    name : str
        The name of the use case.
    includes : list[str], optional
        A list of use cases that this use case includes (default is None).
    extends : list[str], optional
        A list of use cases that this use case extends (default is None).
    Methods
    -------
    display():
        Prints the details of the use case, including its name, included use cases, and extended use cases.
    """
    def __init__(self, name:str, includes:list[str] = None, extends:list[str]= None):
        self.name = name
        self.includes = includes
        self.extends = extends

    def display(self):
        print(f"- {make_bold('Use Case')}: {self.name}")
        
        if self.includes:
            print("Includes:")
            for include in self.includes:
                print(f"--> {include.name}")
        if self.extends:
            print("Extends:")
            for extend in self.extends:
                print(f"<-- {extend.name}")
        print("-----------------")


def generate_use_cases():
    """
    Generates a list of use cases for a system.

    Returns:
        list: A list of Use_Case objects representing different use cases.
            Each Use_Case object may contain sub-use cases.
    """
    return [
    Use_Case("Login", [Use_Case("Verify Login")], [Use_Case("Login Error")]),
    Use_Case("Report Pothole", [Use_Case("Log Pothole")]),
    Use_Case("Report Damage", [Use_Case("Log Damage")]),
    Use_Case("Query PHTRS", [Use_Case("Generate Query Report")]),
    Use_Case("Generat Work Order", [Use_Case("Assign Work Order")]),
   ]



def generate_actors(use_cases):
    """
    Generates a list of Actor objects with predefined roles and associated use cases.

    Returns:
        list: A list of Actor objects, each initialized with a name and a list of use cases.
    """
    return [
    Actor("User", [use_cases[0], use_cases[1], use_cases[2]]),
    Actor("Department Staff", [use_cases[0], use_cases[3], use_cases[4]]),
    Actor("Road Crew", [use_cases[0],use_cases[4].includes[0],use_cases[3]])
    ]

def main_menu():
    """
    Generates:
        clears screen 
        prompts user for input
    Returns:
      int between 0 - 4
    """
    os.system('clear')
    print("Welcome to PHTRS UML Use Case Documentation")
    print("1. Display Use Cases")
    print("2. Display Actors")
    print("3. About")
    print("4. Exit")
    try:
        return int(input("Enter choice: "))
    except ValueError:
        return 0

def print_actors(actors:list[Actor]):
    """
    Generates:
        output of actor.display for all actors
    """
    for actor in actors:
        actor.display()

def print_use_cases(use_cases:list[Use_Case]):
    """
    Generates:
       output of use_case.display for all use_case 
    """
    for use_case in use_cases:
        use_case.display()

def about():
    """
    Prints Program Flow
    """
    print("This program holds UML use case and actor objects for the PHTRS")
    print(f"{make_bold('Program Flow')} ")
    print("------------------")
    print("1. Main Menu")
    print("2. User Selects Menu Item")
    print("3. If 1 is selected prints all use_case objects. Waits for user to press any key. Returns to Main Menu")
    print("4. if 2 is selected prints all actor objects and their associated use_case objects.Waits for user to press any key. Returns to Main Menu")
    print("5. if 3 is selected this about section display (but you already knew that).Waits for user to press any key. Returns to Main Menu")
    print("6. if 4 is selected prints goodbye and exits program")
    print("7. if invalid argument is passed user is notifed of invalid entry and prompted to make another selections.Waits for user to press any key. Returns to Main Menu")
    print("------------------")


def control_loop():
    """
     Generates list of use cases and actors
     Loops : Until option 4 is pressed 
    """
    use_cases = generate_use_cases()
    actors = generate_actors(use_cases)
    while True:
        menu_selection = main_menu()
        if menu_selection == 1:
            print_use_cases(use_cases)
            input("Press enter to continue") 
        elif menu_selection == 2:
            print_actors(actors)
            input("Press enter to continue") 
        elif menu_selection == 3:
            about()  
            input("Press enter to continue")      
        elif menu_selection == 4:
            print("Goodbye")
            exit()
        else:
            print("Invalid selection")
            input("Press enter to continue")

    

    

if __name__ == "__main__":
     control_loop()

    
