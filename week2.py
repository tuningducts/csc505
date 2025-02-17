mport os
from time import sleep

############################################
###### UML Class Definitions ###############
############################################
class Requirements:
    def __init__(self):
        self.id = "Requirements"
        self.inputs = "Stakeholder requirements"
        self.output = "Requirements documenatation"
        self.description = "Gather requirements from stake holders"
        self.calls = ["Design", "Review and Feedback"]
class Feedback:
    def __init__(self): 
        self.id = "Feedback"
        self.inputs = "Requirements Output"
        self.output = "Updated Requirements"
        self.description = "Review and feedback on requirements"
        self.calls = ["Requirements"]
class Design:
    def __init__(self):
        self.id = "Design"
        self.inputs = "Requirements Output"
        self.output = "Application architecture"
        self.description = "Design the application"
        self.calls = ["Prototype", "Feedback"]

class Prototype:
    def __init__(self):
        self.id = "Prototype"
        self.inputs = "Application Architecture"
        self.output = "working prototype"
        self.description = "Create a working prototype"
        self.calls = ["Beta Testing"]

class BetaTesting:
    def __init__(self):
        self.id = "Beta Testing"
        self.inputs = "Working Prototype"
        self.output = "Feedback"
        self.description = "Test the prototype"
        self.calls = ["Implementation","feedback"]

class Implementation:
    def __init__(self):
        self.id = "Implementation"
        self.inputs = "prototype"
        self.output = "source code, unit test, version control"
        self.description = "Implentation"
        self.calls = ["Integration"]

class Integration:
    def __init__(self):
        self.id = "Integration"
        self.inputs = "Tested code, integration plan"
        self.output = "Integrated app,databases,deployment plan"
        self.description = "Integration"
        self.calls = ["Deployment"]
class Deployment:
    def __init__(self):
        self.id = "Deployment"
        self.inputs = "deployment plan, integrated software"
        self.output = "Production software"
        self.description = "Deployment"
        self.calls = ["Review and feedback"]
############################################
###### END UML Class Definitions ###########
############################################


#Handle printing of UML objects     
# takes UML object and prints it to the console
def print_uml(umlObject):
    print(f"""{umlObject.id}
    Inputs: {umlObject.inputs}
    Output: {umlObject.output}
    Description: {umlObject.description}
    Calls: {umlObject.calls}
    """)

# takes users input prints UML object and returns to menu
def handle_menu_selection(selection):
        selection = selection
        print_uml(selection)
        input("press any key to continue")
        menu()

# handles menu controlflow
def menu():
    os.system('clear')
    menu_message = f"""Anschutz Modifed Waterfall
    1 - Requirements
    2 - Feedback
    3 - Design
    4 - Prototyping
    5 - Beta Testing
    6 - Implementation
    7 - Integration
    8 - Deployment
    """
    print(menu_message)
    selection = input("Select Menu Item: ").lower()
    if selection == "1":
         handle_menu_selection(Requirements())
    elif selection == "2":
       handle_menu_selection(Feedback())
    elif selection == "3":  
       handle_menu_selection(Design())
    elif selection == "4": 
        handle_menu_selection(Prototype())
    elif selection == "5":
        handle_menu_selection(BetaTesting())
    elif selection == "6":
        handle_menu_selection(Implementation())
    elif selection == "7":
        handle_menu_selection(Integration())
    elif selection == "8":
        handle_menu_selection(Deployment())
    elif selection == "q":
        print("Have a great day!")
        exit
    else:
        print("invalid selection enter 1,2,3,4,5,6,7,8 or q")
        sleep(2)
        menu()

# main entry point
if __name__ == "__main__":
    menu()
