from time import sleep

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    # Prevent division by zero
    if b == 0:
        return None
    return a / b

def power(a):
    return a ** 2

def get_int(prompt):
    # Safely get an integer from user input
    try:
        return int(input(prompt))
    except ValueError:
        return None


def show_menu():
    print("\nCalculator")
    print("1 -  Add")
    print("2 - Multiply")
    print("3 - Subtract")
    print("4 - Divide")
    print("5 - Power")
    print("0 - Exit")


def main():
    compteur = 0
    while True:
        show_menu()
        choice = input("Choose an option (0-5): ")

        if choice == "0":
            print(f"Goodbye, you did {compteur} operations.")
            break

        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice.")
            continue
        
        if choice == "5":
            a = get_int("First number: ")
            if a is None:
                print("You must enter an integer.")
                sleep(1)
                continue

            result = power(a)
            compteur += 1
            print(f"Result: {result}")
            sleep(1)
            continue
    

        a = get_int("First number: ")
        b = get_int("Second number: ")

        if a is None or b is None:
            print("You must enter integers.")
            sleep(1)
            continue
        if choice == "1":
            result = add(a, b)

        elif choice == "2":
            result = multiply(a ,b)

        elif choice == "3":
            result = subtract(a ,b)

        else:
            result = divide(a ,b)


        if result is None:
            print("Error: division by zero")
            sleep(1)
            continue

        compteur += 1
        print(f"Result: {round(result, 2)}")
        sleep(1)


if __name__ == "__main__":
    main()