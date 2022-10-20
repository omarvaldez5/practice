# ============================================================================ #
# START
# ============================================================================ #

# Function
def two_plus_numbers() -> int:
    """This is a simple function to return the positive sum of two numbers

    Returns:
        int: Positive integer
    """

    try:
        # Description
        print("Welcome! Please, Add two numbers that end up being a positive reuslt\n")

        # Inputs
        param1 = int(input("Enter the first positive number: "))
        param2 = int(input("Enter the second positive number: "))

        # Calculation
        sum_numbers = param1 + param2

        # Constraints
        if sum_numbers > 0:
            print("\nGreat! Your result is the following: ")
        else:
            raise Exception(
                f"You total is {sum_numbers}, which is not a positive number. Please try again.")

    except ValueError as ex:
        print("Remember, you are supposed to enter a positive number! Error: ", ex)
        raise

    return sum_numbers


# ============================================================================ #
# Print Section
# ============================================================================ #
print("\n")
print("*" * 30)
print(two_plus_numbers())
print("*" * 30)
print("\n")

# ============================================================================ #
# END
# ============================================================================ #
