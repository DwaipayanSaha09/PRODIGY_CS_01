def caesar_cipher(text, shift, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - base + shift * (-1 if decrypt else 1)) % 26
            result += chr(base + offset)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ")
        if choice.lower() == 'q':
            break
        if choice.lower() not in ['e', 'd']:
            print("Invalid choice. Please try again.")
            continue
        
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))
        
        if choice.lower() == 'e':
            encrypted_text = caesar_cipher(text, shift)
            print("Encrypted text:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, shift, decrypt=True)
            print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()


