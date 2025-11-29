#!/usr/bin/env python3

def conversions():
    while True:
        print("\nConversion menu:")
        print("1. Hours → Minutes")
        print("2. Kilometers → Meters")
        print("3. Celsius → Fahrenheit")
        print("4. Back")

        choice = input("Choose (1-4): ").strip()
        if choice == "4":
            return
        if choice == "1":
            try:
                hrs = float(input("Hours: "))
            except ValueError:
                print("Enter a valid number.")
                continue
            print(f"{hrs} hrs = {hrs * 60} minutes")
        elif choice == "2":
            try:
                km = float(input("Kilometers: "))
            except ValueError:
                print("Enter a valid number.")
                continue
            print(f"{km} km = {km * 1000} meters")
        elif choice == "3":
            try:
                c = float(input("Celsius: "))
            except ValueError:
                print("Enter a valid number.")
                continue
            print(f"{c}°C = {(c * 9/5) + 32}°F")
        else:
            print("Invalid choice, try again.")

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Conversions")
        print("6. Quit")

        choice = input("Choose (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        if choice == "5":
            conversions()
            continue
        if choice not in ("1","2","3","4"):
            print("Invalid choice.")
            continue

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b == 0:
                print("Error: division by zero")
            else:
                print("Result:", a / b)

if __name__ == "__main__":
    calculator()
