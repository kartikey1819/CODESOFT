import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if len(characters) == 0:
        return "Error: No characters selected for password generation."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(" Welcome to Password Generator Application, start generating random password: ")
    try:
        length = int(input("Enter the required length of your password: "))
        use_uppercase = input("would you like to Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("would you like to Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("would you like to Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("would you like to Include special characters? (yes/no): ").lower() == 'yes'
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
if __name__ == "__main__":
    main()
