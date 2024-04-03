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
        print("\nOptions:")
        print("1. Generate Password")
        print("2. Exit")
        choice = input("Please enter your choice (1 or 2): ")

        if choice == '1':
            num_passwords = int(input("Enter the number of passwords to generate (default is 1): ") or 1)
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
            
            filename = input("Enter the filename to save the passwords (e.g., passwords.txt): ")
            with open(filename, 'w') as f:
                for password in passwords:
                    f.write(password + '\n')
                print(f"{num_passwords} password(s) saved to {filename}")
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
