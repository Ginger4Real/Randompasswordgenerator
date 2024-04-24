import random
import string
import os

def generate_password(length=10, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    characters = ''

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += '!@%'

    if not characters:
        print("Please select at least one character type.")
        return None

    # Ensure there is at least one special character in the password
    if use_special_chars:
        password = random.choice('!@%') + ''.join(random.choices(characters, k=length - 1))
    else:
        password = ''.join(random.choices(characters, k=length))

    return password

def save_passwords(passwords, filename):
    try:
        with open(filename, 'w') as f:
            for password in passwords:
                f.write(password + '\n')
            print(f"{len(passwords)} password(s) saved to {filename}")
    except IOError:
        print("Error: Unable to save passwords to the file.")

def load_passwords(filename):
    passwords = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                passwords.append(line.strip())
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Unable to load passwords from the file.")
    return passwords

def main():
    print("Welcome to the Random Password Generator!")
    language_choice = input("Choose your language (English/Dutch): ").lower()

    if language_choice.startswith('d'):  # Dutch language
        print("\nWelkom bij de Willekeurige Wachtwoord Generator!")
        options = {
            '1': "Genereer Wachtwoord",
            '2': "Wachtwoorden Opslaan naar Bestand",
            '3': "Wachtwoorden Laden van Bestand",
            '4': "Exit"
        }
        prompts = {
            '1': "",  # No prompt needed for generating passwords
            '2': "Voer het aantal wachtwoorden in om op te slaan (standaard is 1): ",
            '3': "Voer de bestandsnaam in om wachtwoorden van te laden: "
        }
    else:  # English language (default)
        print("\nWelcome to the Random Password Generator!")
        options = {
            '1': "Generate Password",
            '2': "Save Passwords to File",
            '3': "Load Passwords from File",
            '4': "Exit"
        }
        prompts = {
            '1': "",  # No prompt needed for generating passwords
            '2': "Enter the number of passwords to save (default is 1): ",
            '3': "Enter the filename to load passwords from: "
        }

    while True:
        print("\nOptions:")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Please enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            length = int(input("Enter the length of each password (default is 10): ") or 10)
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include digits? (y/n): ").lower() == 'y'
            use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

            passwords = []
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
            if password:
                passwords.append(password)

            print("\nGenerated Password:")
            for password in passwords:
                print(password)

        elif choice == '2':
            num_passwords = int(input(prompts['2']) or 1)
            passwords = [input("Enter the password to save: ") for _ in range(num_passwords)]
            filename = input("Enter the filename to save the passwords (e.g., passwords.txt): ")
            save_passwords(passwords, filename)

        elif choice == '3':
            filename = input(prompts['3'])
            passwords = load_passwords(filename)
            print("\nLoaded Passwords:")
            for password in passwords:
                print(password)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
