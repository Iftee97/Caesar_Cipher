# importing alphabets from alphabet.py
from alphabet import alphabets

# importing logo from art.py
from art import logo
print(logo)

print("\n---[welcome to the text encoder]---")

def caesar():
    should_continue = True

    while should_continue:

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("enter text: ").lower()
        shift = int(input("enter shift number: "))

        transformed_text = ''

        for char in text:
            if char in alphabets:
                index = alphabets.index(char)
                if direction == 'encode':
                    index += shift
                    
                elif direction == 'decode':
                    index -= shift

                transformed_text += alphabets[index]

            else:
                transformed_text += char

        print(f'transformed text: {transformed_text}\n')

        choice = input("whould you like to go again? ['yes'] / ['no']\n")
        if choice == 'no':
            should_continue = False
            print('Goodbye!')

caesar()