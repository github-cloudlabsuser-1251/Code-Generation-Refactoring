# A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX_ELEMENTS = 100

def calculate_sum(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)

def get_number_of_elements():
    """Prompts the user for the number of elements and validates the input."""
    while True:
        try:
            n = int(input(f"Enter the number of elements (1-{MAX_ELEMENTS}): "))
            if 1 <= n <= MAX_ELEMENTS:
                return n
            else:
                print(f"Please enter a number between 1 and {MAX_ELEMENTS}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_elements(n):
    """Prompts the user to enter n integers and returns them as a list."""
    numbers = []
    print(f"Enter {n} integers:")
    while len(numbers) < n:
        try:
            num = int(input(f"Element {len(numbers)+1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return numbers

def main():
    try:
        n = get_number_of_elements()
        numbers = get_elements(n)
        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
