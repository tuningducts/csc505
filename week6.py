import os

class NumberToWordsConverter:
    """
    A class to convert numbers into their word representation.

    Methods
    -------
    convert_number_to_words(n: int) -> str
        Convert a number into words (supports 0 <= n < 1000 for this example).
        Parameters:
            n (int): The number to convert.
        Returns:
            str: The word representation of the number.
    """
    def convert_number_to_words(self, n: int) -> str:
        """Convert a number into words (supports 0 <= n < 1000 for this example)."""
        ones = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        ]
        tens = [
            "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
        ]

        if n < 20:
            return ones[n]
        elif n < 100:
            return f"{tens[n // 10]}{('' if n % 10 == 0 else ' ' + ones[n % 10])}"
        elif n < 1000:
            result = f"{ones[n // 100]} hundred"
            remainder = n % 100
            if remainder:
                result += f" {self.convert_number_to_words(remainder)}"
            return result
        elif n < 10000:
            result = f"{ones[n // 1000]} thousand"
            remainder = n % 1000
            if remainder:
                result += f" {self.convert_number_to_words(remainder)}"
            return result

        else:
            # For simplicity, numbers 1000 or above are returned as a string.
            return str(n)


class AmountConverter:
    """
    AmountConverter is a class that provides methods to convert numerical dollar and cent amounts into their corresponding words representation.
    Methods:
        __init__():
            Initializes the AmountConverter instance and sets up the NumberToWordsConverter.
        convert_dollars_to_words(dollars: int) -> str:
            Converts a given dollar amount to its words representation.
            Args:
                dollars (int): The dollar amount to be converted.
            Returns:
                str: The words representation of the dollar amount.
        convert_cents_to_words(cents: int) -> str:
            Converts a given cents amount to its words representation.
            Args:
                cents (int): The cents amount to be converted.
            Returns:
                str: The words representation of the cents amount.
        combine_words(dollars_words: str, cents_words: str) -> str:
            Combines the words representation of dollars and cents into a full check amount string.
            Args:
                dollars_words (str): The words representation of the dollar amount.
                cents_words (str): The words representation of the cents amount.
            Returns:
                str: The combined words representation of the full check amount.
    """
    def __init__(self):
        self.number_converter = NumberToWordsConverter()
        self.LINE_LENGTH = 75

    def convert_dollars_to_words(self, dollars: int) -> str:
        return(self.number_converter.convert_number_to_words(dollars))

    def convert_cents_to_words(self, cents: int) -> str:
        return(self.number_converter.convert_number_to_words(cents))
    

    def combine_words(self, dollars_words: str, cents_words: str) -> str:
        combined = f"{dollars_words} dollars and {cents_words} cents" 
        dashes = '-'  * max(0,self.LINE_LENGTH - len(combined))
        return f"{combined}{dashes}"


class CheckWriter:
    """
    CheckWriter is a class that handles the conversion of numeric dollar amounts into their written words form for check writing purposes.
    Attributes:
        amount (float): The dollar amount to be converted and printed on the check.
        converter (AmountConverter): An instance of the AmountConverter class used to convert numeric amounts to words.
    Methods:
        __init__():
            Initializes the CheckWriter with a default amount of 0.0 and an instance of AmountConverter.
        read_amount() -> float:
            Reads the dollar amount from user input and updates the amount attribute. 
            Returns the amount as a float. If the input is invalid, defaults the amount to 0.0.
        convert_amount() -> str:
            Converts the numeric amount to its written words form. 
            Returns the amount in words as a string.
        print_check():
            Prints the check with the amount in words.
    """
    def __init__(self):
        self.amount: float = 0.0  
        self.converter = AmountConverter()  

    def read_amount(self) -> float:
        try:
            self.amount = float(input("Enter the amount: "))
            if self.amount > 10000:
                print("Amount must be below 9999.99")
                self.amount = 0.00
        except ValueError:
           print("Invalid input. Defaulting amount to 0.0")
           self.amount = 0.00
        return self.amount

    def convert_amount(self) -> str:
        dollars = int(self.amount)
        dollars_words = self.converter.convert_dollars_to_words(dollars)
        # Calculate cents (rounded to nearest whole number)
        cents = int(round((self.amount - dollars) * 100))
        cents_words = self.converter.convert_cents_to_words(cents)
        return self.converter.combine_words(dollars_words, cents_words)
     

    def print_check(self):
        amount_in_words = self.convert_amount()
        print("Check Amount:", amount_in_words)


class RunCheckWriter:
    """
    RunCheckWriter is a class that runs the check writer program. 
    Attributes:
        writer(CheckWriter())
    Methods:
        __init__():
            initialize writer object
        main_menu() -> int:
            displays menu option to user 
            Returns user menu option as int
        run():
            Control loop for program
       about():
          Prints information about the program 
    """
    def __init__(self):
        self.writer = CheckWriter()
       
    def main_menu(self):
        """
        Generates:
            clears screen 
            prompts user for input
        Returns:
        int between 0 - 4
        """
        os.system('clear')
        print("Welcome to Check Writer")
        print("1. Write Check")
        print("2. About")
        print("3. Exit")
        try:
            return int(input("Enter choice: "))
        except ValueError:
            return 0
    def about(self):
        print("This program takes a dollar amount and print the amount as a string")
        print("1. Select option from main menu")
        print("2. program creates CheckWriter object")
        print("3. program takes input")
        print("4. program takes input as 9999.99")
        print("5.program converts amount to string CheckWriter --> AmountConverter -- >NumberToWordsConverter ")
        print("6.program returns amount as string ")
        print("7. if user selcts option 2 porgram prints this about section. ")
        print("8. if user selects option 3 program exits")
        print("9. if user input invalid option program notifies user")


    def run(self):
        while True:
            menu_selection = self.main_menu()
            if menu_selection == 1:
                writer = CheckWriter()
                writer.read_amount()    # Prompt user for amount
                writer.print_check()
                input("Press enter to continue") 
            elif menu_selection == 2:
                self.about()
                input("Press enter to continue") 
            elif menu_selection == 3:
                print("Goodbye")
                exit()
            else:
                print("Invalid selection")
                input("Press enter to continue")


# Example usage:
if __name__ == "__main__":
    program = RunCheckWriter()
    program.run()
