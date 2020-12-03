alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("\n---[welcome to the text encoder]---")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("enter text: ").lower()
shift = int(input("enter shift number: "))

def encrypt(text, shift):
    encrypted_text = ''
    for letter in text:
        index = alphabet.index(letter)
        index += shift
        encrypted_text += alphabet[index]
    print(encrypted_text)

def decrypt(text, shift):
    decrypted_text = ''
    for letter in text:
        index = alphabet.index(letter)
        index -= shift
        decrypted_text += alphabet[index]
    print(f"decrypted text: {decrypted_text}")

if direction == 'encode':
    encrypt(text, shift)
    
elif direction == 'decode':
    decrypt(text, shift)