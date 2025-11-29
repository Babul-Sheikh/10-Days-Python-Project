#!/usr/bin/env python3

def main():
    print("Simple Calculator")
    while True:
        op = input("Choose operation (+ - * /) or q to quit: ").strip()
        if op.lower() == 'q':
            print("Goodbye!")
            break
        if op not in ('+', '-', '*', '/'):
            print("Invalid operation. Try again.")
            continue

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if op == '/' and b == 0:
            print("Error: division by zero")
            continue

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        else:
            result = a / b

        print("Result:", result)

if __name__ == '__main__':
    main()
