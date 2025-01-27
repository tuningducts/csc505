import random 
from time import sleep
import os

#generates a cat wiht a random name, personality, and breed
class Cat:
    def __init__(self, name, personality,species):
        self.name = name
        self.personality = personality
        self.species = species
    def get_name(self):
        return self.name
         



class CatGenie:
    def __init__(self):
        self.cats = []
        self.cat_names =["Whisker McFluff", "Sir Purrs-a-Lot", "Meowly Cyrus", "Purrlock Holmes", "Fuzz Aldrin", "Cat Damon", "Cleocatra", "Purrito", "Kit-Kat"]
        self.personalities = ["Playful", "Lazy", "Curious", "Affectionate", "Independent"]
        self.breeds = ["Persian", "Maine Coon", "Siamese", "Ragdoll", "Bengal", "Sphynx", "British Shorthair", "Abyssinian", "Scottish Fold", "Burmese"]
        self.wishes = 3

    def use_wish(self):
        self.wishes -= 1 
    
    def generate_cat(self):
        if self.wishes > 0:
            self.use_wish()
            cat = Cat(self.generate_cat_name(), self.generate_cat_personality(), self.generate_cat_breed())
            self.cats.append(cat)
            print(f"Your wish is my command. I have created a {cat.species} named {cat.name} with a {cat.personality} peronsality ")
            return cat
        else:
            print("You used up all your wishes. I could generate another cat but I am not obligated to. ")

    def list_cats(self):
        if  not self.cats:
            print("I haven't created any cats for you.")
        else:
            print("I have created the following cats")
            for cat in self.cats:
                print(f'{cat.name} is a {cat.personality} {cat.species}')
    
    def generate_cat_name(self):
        name = random.choice(self.cat_names)
        self.cat_names.remove(name)
        return name

    def generate_cat_personality(self):
        return random.choice(self.personalities)
    
    def generate_cat_breed(self):
        return random.choice(self.breeds)                

     
    

def menu():
    os.system('clear')
    menu_message = f"""Cat genie Menu
    1 - Create Cat
    2 - List Cats
    q - exit
    """
    print(menu_message)
    selection = input("Select Menu Item: ").lower()
    if selection == "1":
        catGenie.generate_cat()
        input("press any key to continue")
        menu()
    elif selection == "2":
        catGenie.list_cats()
        input("press any key to continue")
        menu()
    elif selection == "q":
        print("Have a great day!")
        exit
    else:
        print("invalid selection enter 1,2, or q")
        sleep(2)
        menu()


if __name__ == "__main__":
    print("welcome to Cat Genie")
    catGenie = CatGenie()
    menu()
    #menu = Menu()
    #menu.display_menu()
    
    
    

