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
        characters += string.punctuation
    
    if not characters:
        print("Please select at least one character type.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    while True:
        print("\nLanguage Options:")
        print("1. English")
        print("2. Dutch")
        language_choice = input("Please choose your language (1 for English, 2 for Dutch): ")
        
        if language_choice == '1':
            prompts = {
                "generate": "Generate Password",
                "exit": "Exit",
                "num_passwords": "Enter the number of passwords to generate (default is 1): ",
                "length": "Enter the length of each password (default is 10): ",
                "uppercase": "Include uppercase letters? (y/n): ",
                "lowercase": "Include lowercase letters? (y/n): ",
                "digits": "Include digits? (y/n): ",
                "special_chars": "Include special characters? (y/n): ",
                "filename": "Enter the filename to save the passwords (e.g., passwords.txt): ",
                "saved": "{} password(s) saved to {}",
                "invalid_choice": "Invalid choice. Please enter 1 or 2."
            }
            break
        elif language_choice == '2':
            prompts = {
                "generate": "Genereer Wachtwoord",
                "exit": "Afsluiten",
                "num_passwords": "Voer het aantal te genereren wachtwoorden in (standaard is 1): ",
                "length": "Voer de lengte van elk wachtwoord in (standaard is 10): ",
                "uppercase": "Inclusief hoofdletters? (j/n): ",
                "lowercase": "Inclusief kleine letters? (j/n): ",
                "digits": "Inclusief cijfers? (j/n): ",
                "special_chars": "Inclusief speciale tekens? (j/n): ",
                "filename": "Voer de bestandsnaam in om de wachtwoorden op te slaan (bijv. wachtwoorden.txt): ",
                "saved": "{} wachtwoord(en) opgeslagen naar {}",
                "invalid_choice": "Ongeldige keuze. Voer alstublieft 1 of 2 in."
            }
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("\n{}".format(prompts["welcome"]))
    
    while True:
        print("\nOptions:")
        print("1. {}".format(prompts["generate"]))
        print("2. {}".format(prompts["exit"]))
        choice = input("{}".format(prompts["choice"]))

        if choice == '1':
            num_passwords = int(input(prompts["num_passwords"]) or 1)
            length = int(input(prompts["length"]) or 10)
            use_uppercase = input(prompts["uppercase"]).lower() == 'y'
            use_lowercase = input(prompts["lowercase"]).lower() == 'y'
            use_digits = input(prompts["digits"]).lower() == 'y'
            use_special_chars = input(prompts["special_chars"]).lower() == 'y'
            
            passwords = []
            for _ in range(num_passwords):
                password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
                if password:
                    passwords.append(password)
            
            filename = input(prompts["filename"])
            with open(filename, 'w') as f:
                for password in passwords:
                    f.write(password + '\n')
                print(prompts["saved"].format(num_passwords, filename))
        elif choice == '2':
            print("{}".format(prompts["exit_message"]))
            break
        else:
            print("{}".format(prompts["invalid_choice"]))

if __name__ == "__main__":
    main()
