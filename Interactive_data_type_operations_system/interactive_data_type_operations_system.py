RED = '\033[91m'
GREEN = '\033[92m'
ORANGE = '\033[38;2;255;165;0m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Prompt the user to choose a data type to perform operations on
print(f"{CYAN}============================{RESET}")
print(f"{ORANGE}Choose a data type to perform operations on:{RESET}")
print(f"{BLUE}1.{MAGENTA} Strings{RESET}")
print(f"{BLUE}2.{MAGENTA} Numbers{RESET}")
print(f"{BLUE}3.{MAGENTA} Booleans{RESET}")
print(f"{BLUE}4.{MAGENTA} Additional Data Types {RESET}({ORANGE}List, Tuple, Dictionary{RESET})")
print(f"{CYAN}============================{RESET}")

while True:
    # Get the user's choice and store it in a variable
    choice = input(f"{ORANGE}Enter the number of your choice ({BLUE}1-4{RESET}): ")

    # If the user chooses Strings (choice == '1'):
    if choice == '1':
        print(f"{GREEN}You chose {ORANGE}strings{RESET}.")
        print(f'{CYAN}----------------------------{RESET}')
        # Declare a string variable, e.g., sentence = "Learning Python is fun!"
        sentence = "Learning Python is fun!"
        print(f"{YELLOW}String:{RESET} \"{sentence}\"")
        # Extract and print a substring, such as the word "Python" from the sentence.
        python_word = sentence[3:12]
        print(f"{YELLOW}Substring:{RESET}", python_word)

        # Convert the entire sentence to uppercase and print it.
        uppercase_sentence = sentence.upper()
        print(f"{YELLOW}Uppercase sentence:{RESET}", uppercase_sentence)

        # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.
        modified_sentence = sentence.replace("fun", "awesome")
        print(f"{YELLOW}Modified sentence:{RESET}", modified_sentence)

        # Print the length of the string
        print(f"{YELLOW}Length of the string:{RESET}", len(sentence))

    # If the user chooses Numbers (choice == '2'):
    elif choice == '2':
        # Prompt the user to input two numbers, e.g., num1 and num2.
        print(f"{GREEN}You chose {ORANGE}numbers{RESET}.")
        print(f'{CYAN}----------------------------{RESET}')
        num1 = int(input(f"{GREEN}Enter the first number:{RESET} "))
        num2 = int(input(f"{GREEN}Enter the second number:{RESET} "))

        # Perform and print the results of addition, subtraction, multiplication, and division.
        print(f"{YELLOW}Addition:{RESET} {num1 + num2}")
        print(f"{YELLOW}Subtraction:{RESET} {num1 - num2}")
        print(f"{YELLOW}Multiplication:{RESET} {num1 * num2}")

        # Handle division by zero (e.g., print an error message if num2 is zero).
        try:
            print(f"{YELLOW}Division:{RESET} {num1 / num2}")
        except ZeroDivisionError as e:
            print(f"{RED}Error:{RESET} Division by zero is not allowed.")

        # Perform a power operation, raising num1 to the power of num2, and print the result.
        print(f'{num1} {YELLOW}raised to the power of{RESET} {num2} {YELLOW}is{RESET}: {num1 ** num2}')

    # If the user chooses Booleans (choice == '3'):
    elif choice == '3':
        print(f"{GREEN}You chose {ORANGE}booleans{RESET}.")
        print(f'{CYAN}----------------------------{RESET}')
        # Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
        is_python_fun = True
        is_sunny = False
        print(f"{YELLOW}Boolean Variables:{RESET}")
        print(f"{YELLOW}is_python_fun:{RESET}", is_python_fun)
        print(f"{YELLOW}is_sunny:{RESET}", is_sunny)
        # Perform and print the results of logical operations: AND, OR, NOT.
        print(f"{YELLOW}AND:{RESET}", is_python_fun and is_sunny)
        print(f"{YELLOW}OR:{RESET}", is_python_fun or is_sunny)
        print(f"{YELLOW}NOT:{RESET}", not is_python_fun)

        # Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).
        print(f"{YELLOW}Comparison:{RESET}", 10 > 5 and 5 == 5)

    # If the user chooses Additional Data Types (choice == '4'):
    elif choice == '4':
        # ### List Operations ###
        print(f"{GREEN}You chose {ORANGE}additional data types{RESET}.")
        print(f'{CYAN}----------------------------{RESET}')
        # Create a list with mixed data types (e.g., numbers, strings, booleans).
        my_list = [1, "Python", True, 3.14, "AI"]
        print(f"{YELLOW}Initial List:{RESET}", my_list)

        # Append a new element to the list and print the updated list.
        my_list.append("Programming")
        print(f"{YELLOW}Updated List:{RESET}", my_list)

        # Access and print the 4th element in the list.
        print(f"{YELLOW}4th Element in List:{RESET}", my_list[3])

        # ### Tuple Operations ###
        # Create a tuple with some string elements (e.g., fruits).
        fruits_tuple = ("apple", "banana", "cherry")
        print(f"{YELLOW}Initial Tuple:{RESET}", fruits_tuple)

        # Print the length of the tuple.
        print(f"{YELLOW}Length of Tuple:{RESET}", len(fruits_tuple))

        # Try to modify one element in the tuple and handle the resulting TypeError.
        try:
            fruits_tuple[0] = "orange"
        except TypeError as e:
            print(f"{RED}Error:{RESET} Tuples are immutable. Cannot modify elements.")

        # ### Dictionary Operations ###
        # Create a dictionary with some key-value pairs (e.g., name, age, city).
        person_dict = {"name": "John", "age": 30, "city": "New York"}
        print(f"{YELLOW}Initial Dictionary:{RESET}", person_dict)
        # Print the keys and values in the dictionary.
        print(f"{YELLOW}Keys and Values in Dictionary:{RESET}")
        for key, value in person_dict.items():
            print(f"{GREEN}{key}:{RESET} {value}")
        # Access and print the value for one of the keys (e.g., "age").
        print(f"{YELLOW}Age:{RESET}", person_dict["age"])

        # Add a new key-value pair to the dictionary and print the updated dictionary.
        person_dict["profession"] = "Engineer"
        print(f"{YELLOW}Updated Dictionary:{RESET}", person_dict)

    # If the user enters an invalid choice:
    else:
        print(f"{RED}Error:{RESET} Invalid choice. Please choose a valid data type (1-4).")
    print(f'{CYAN}----------------------------{RESET}')