RED = '\033[91m'
GREEN = '\033[92m'
ORANGE = '\033[38;2;255;165;0m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'


# Prompt the user to choose a data type to perform operations on
print(f"{ORANGE}Choose{RESET} a data type to perform operations on:")
print(f"{BLUE}1.{ORANGE} Strings{RESET}")
print(f"{BLUE}2.{ORANGE} Numbers{RESET}")
print(f"{BLUE}3.{ORANGE} Booleans{RESET}")
print(f"{BLUE}4.{ORANGE} Additional Data Types {RESET}({ORANGE}List, Tuple, Dictionary{RESET})")

while True:
    # Get the user's choice and store it in a variable
    choice = input(f"{ORANGE}Enter{RESET} the number of your choice ({BLUE}1-4{RESET}): ")

    # If the user chooses Strings (choice == '1'):
    if choice == '1':
        print(f"You choose {ORANGE}strings{RESET}.")
        # Declare a string variable, e.g., sentence = "Learning Python is fun!"
        sentence = "Learning Python is fun!"
        print(f"{ORANGE}String:{RESET} \"Learning Python is fun!\"")
        # Extract and print a substring, such as the word "Python" from the sentence.
        python_word = sentence[5:13]
        print(f"{ORANGE}Substring:{RESET}", python_word)

        # Convert the entire sentence to uppercase and print it.
        uppercase_sentence = sentence.upper()
        print(f"{ORANGE}Uppercase sentence:{RESET}", uppercase_sentence)

        # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.
        modified_sentence = sentence.replace("fun", "awesome")
        print(f"{ORANGE}Modified sentence:{RESET}", modified_sentence)

        # Print the length of the string
        print(f"{ORANGE}Length of the string:{RESET}", len(sentence))

    # If the user chooses Numbers (choice == '2'):
    elif choice == '2':
        # Prompt the user to input two numbers, e.g., num1 and num2.
        num1 = int(input(f"{ORANGE}Enter{RESET} the first number: "))
        num2 = int(input(f"{ORANGE}Enter{RESET} the second number: "))

        # Perform and print the results of addition, subtraction, multiplication, and division.
        if num2 != 0:
            print(f"{ORANGE}Addition:{RESET} ", num1 + num2)
            print(f"{ORANGE}Subtraction:{RESET} ", num1 - num2)
            print(f"{ORANGE}Multiplication:{RESET} ", num1 * num2)
            print(f"{ORANGE}Division:{RESET} ", num1 / num2)
        # Handle division by zero (e.g., print an error message if num2 is zero).
        else:
            print("Error: Division by zero is not allowed.")

        # Perform a power operation, raising num1 to the power of num2, and print the result.
        print(f'{num1} raised to the power of {num2} is: {num1 ** num2}')

    # If the user chooses Booleans (choice == '3'):
    elif choice == '3':
        # Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
        is_python_fun = True  # Correct assignment using '='
        is_sunny = False  # Correct assignment using '='

        # Perform and print the results of logical operations: AND, OR, NOT.
        print("AND: ", is_python_fun and is_sunny)
        print("OR: ", is_python_fun or is_sunny)
        print("NOT: ", not is_python_fun)

        # Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).
        print("Comparison: ", 10 > 5 and 5 == 5)

    # If the user chooses Additional Data Types (choice == '4'):
    elif choice == '4':
        print("Additional Data Types (List, Tuple, Dictionary) coming soon...")
    # ### List Operations ###
    # Create a list with mixed data types (e.g., numbers, strings, booleans).

    # Append a new element to the list and print the updated list.

    # Access and print the 4th element in the list.

    # ### Tuple Operations ###
    # Create a tuple with some string elements (e.g., fruits).

    # Print the length of the tuple.

    # Try to modify one element in the tuple and handle the resulting TypeError.

    # ### Dictionary Operations ###
    # Create a dictionary with some key-value pairs (e.g., name, age, city).

    # Access and print the value for one of the keys (e.g., "age").

    # Add a new key-value pair to the dictionary and print the updated dictionary.
    # If the user enters an invalid choice:
    else:
        print("Error: Invalid choice. Please choose a valid data type (1-4).")
