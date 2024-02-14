import random
import string


def generate_password(length, complexity):
    characters = ""

    if complexity == 1:
        characters += string.ascii_lowercase
    if complexity == 2:
        characters += string.ascii_uppercase
        characters += string.ascii_lowercase
    if complexity == 3:
        characters += string.ascii_uppercase
        characters += string.ascii_lowercase
        characters += string.digits
    if complexity == 4:
        characters += string.ascii_uppercase
        characters += string.ascii_lowercase
        characters += string.digits
        characters += "!@#$%^&"

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password


def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))

        print("Select complexity options:")
        print("1. Weak")
        print("2. Good")
        print("3. Strong")
        print("4.Super strong")

        complexity = int(input(""))

        generated_password = generate_password(length, complexity)

        if generated_password:
            print("Generated Password:", generated_password)
    except TypeError:
        print("Please type numbers only!")


if __name__ == "__main__":
    main()
