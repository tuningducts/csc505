import os
import random
class Personality:
    """
    A class to represent a Peronsality Trait.

    Attributes:
    ----------
    name : str
        The name of the Trait
    personalities : list[Personality]
        A list of attributes associated with the trait.

    Methods:
    -------
    display():
        Prints the details of the trait and its attributes.
    """
    def __init__(self, name:str, attributes:list[str]):
        self.id = name
        self.attributes = attributes

    def display(self):
        print(f"{self.id}")
        print("-----------------")
        for attribute in self.attributes:
            print(f"- {attribute}")
        print("-----------------")  
        

class SoftwareEngineer:
    """
    A class to represent a Software Engineer.

    Attributes:
    ----------
    name : str
        The name of the software engineer.
    personalities : list[Personality]
        A list of Personality objects associated with the software engineer.

    Methods:
    -------
    display():
        Prints the details of the software engineer and their personalities.
    """
    def __init__(self, name:str, personalites:list[Personality]):
        self.name = name
        self.personalities = personalites

    def display(self):
        print(f"Software Engineer: {self.name}")
        print("-----------------")
        for personality in self.personalities:
            personality.display()
        print("-----------------")



def generate_traits():
    """
    Generates a list of Personality objects 
    Returns:
        list: A list of Personality objects
    """
    return [
        Personality("Individual Responsibility", ["self motivated", "delivers on time", "takes intiative"]),
        Personality("Acute Awareness", ["Empathy","understands requirements"]),
        Personality('Brutal Honesty', ["direct", "transparent", "finds flaws"]),
        Personality("Resilience Under Pressure", ["calm", "focused", "problem solver"]),
        Personality("Sense of Fairness", ["equitable", "just", "impartial"]),
        Personality("Attention to Detail", ["meticulous", "thorough", "precise"]),
        Personality("Pragmatism", ["realistic", "practical", "sensible"]),
        Personality("Creativity", ["innovative", "imaginative", "original"])
    ]


def menu():
    """
    Displays a menu for the Software Engineer Generator program and prompts the user for a selection.
    The menu options are:
    1. Generate Software Engineer with Random Traits
    2. Display Software Engineer
    3. About
    4. Exit
    Returns:
        int: The user's menu selection as an integer. If the input is not a valid integer, returns 0.
    """
 
    os.system('clear')
    print("Software Engineer Generator")
    print("1. Generate Software Engineer with Random Traits")
    print("2. Display Software Engineer")
    print("3. About")
    print("4. Exit")

    try:
        return int(input("Enter selection: "))
    except ValueError:
        return 0
        

def about():
    """
    Displays information about the program.
    assignment requirement 
    """
    print("About")
    print("-----------------")
    print("This program generates a software engineer with random traits.")
    print("The engineer will have 3 random traits from the following list:")
    print("\n".join(f"- {trait.id}" for trait in traits))   
    print("Generated engineers overwrite any previously generated engineer.")
    print("Selecting display will show the name of the engineer and their traits.")
    print("Selecting exit will close the program. Enginner will not be saved.")
    print("-----------------")
    input("Press enter to continue")

# Generate a software engineer with random traits
def generate_engineer():
    """
    Generates a SoftwareEngineer object with random traits.
    Returns:
        SoftwareEngineer: A SoftwareEngineer object
    """
    name = input("Enter the name of the engineer: ")
    personalities = random.sample(traits, 3)
    return SoftwareEngineer(name, personalities)
    
def program_loop():
    while True:
        menu_selection = menu()
        if menu_selection == 1:
            engineer = generate_engineer()
            print("Engineer created")
            input("Press enter to continue")
        elif menu_selection == 2:
            engineer.display()
            input("Press enter to continue")   
        elif menu_selection == 3:
            about()          
        elif menu_selection == 4:
            print("Goodbye")
            exit()
        else:
            print("Invalid selection")
            input("Press enter to continue")
    

#main program loop
if __name__ == "__main__":
    traits = generate_traits()
    program_loop()
    
