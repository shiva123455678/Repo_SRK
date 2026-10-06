#!/usr/bin/env python3
import re

def evaluate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Invalid syntax"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Python Calculator")
    print("=" * 40)
    print("Supported operations: +, -, *, /, //, %, **")
    print("Type 'exit' or 'quit' to exit\n")

    while True:
        try:
            user_input = input(">>> ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break

            result = evaluate(user_input)
            print(f"= {result}\n")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    main()
