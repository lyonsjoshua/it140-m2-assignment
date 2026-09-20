"""Calculate the user's birth year from their name and age.

Input:
    User's name as a string from the keyboard.
    User's age as an integer from the keyboard.

Process:
    Subtract the user's age from the current year.

Output:
    A personalized message with the user's name and birth year.

Typical usage example:
    What is your name? Joshua
    How old are you? 32
    Hello Joshua! You were born in 1994.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===


