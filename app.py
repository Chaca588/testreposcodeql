import random

def main():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    # Check if the number is even or odd
    result = "even" if random_number % 2 == 0 else "odd"

    # Print the random number and the result
    print(f"Generated random number: {random_number}")
    print(f"The number is {result}.")

if __name__ == "__main__":
    main()
