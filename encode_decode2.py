alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("\n---[welcome to the text encoder]---")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("enter text: ").lower()
shift = int(input("enter shift number: "))

def caesar(text, shift, direction):
    transformed_text = ''

    for letter in text:
        index = alphabet.index(letter)
        
        if direction == 'encode':
            index += shift
        
        elif direction == 'decode':
            index -= shift

        transformed_text += alphabet[index]
    print(f'transformed text: {transformed_text}')

caesar(text, shift, direction)