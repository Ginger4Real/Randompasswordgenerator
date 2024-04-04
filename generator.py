import random
import string

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
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_passwords(passwords, filename):
    with open(filename, 'w') as f:
        for password in passwords:
            f.write(password + '\n')
        print(f"{len(passwords)} password(s) saved to {filename}")

def load_passwords(filename):
    passwords = []
    with open(filename, 'r') as f:
        for line in f:
            passwords.append(line.strip())
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
            '1': "Voer het aantal wachtwoorden in om te genereren (standaard is 1): ",
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
            '1': "Enter the number of passwords to generate (default is 1): ",
            '2': "Enter the number of passwords to save (default is 1): ",
            '3': "Enter the filename to load passwords from: "
        }
    
    while True:
        print("\nOptions:")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Please enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            num_passwords = int(input(prompts['1']) or 1)
            length = int(input("Enter the length of each password (default is 10): ") or 10)
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include digits? (y/n): ").lower() == 'y'
            use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
            
            passwords = []
            for _ in range(num_passwords):
                password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
                if password:
                    passwords.append(password)
            
            print("\nGenerated Passwords:")
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
