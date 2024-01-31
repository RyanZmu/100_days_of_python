"""
Caesar Cipher!
"""

"""
Create a Caesar Cipher by shift the alphabet by the input value

Example:
ABC with Shift = 1
BCD

Functionality:
Type encode to encrypt or decode to decrypt
Type the shift number
Return result
Y or N to restart if you want to decode the string you just encoded
"""
alphabet: list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]

user_choice: str = input("Type 'encode' to encrypt a string or 'decode' to decrypt a string\n")
user_string: str = input("Type your message\n").lower()
shift: int = int(input("Type the shift amount\n"))


# Functions work for test cases, does not always work correctly aside from test cases, refactor.
def encrypt(string, shift_amount):
    original_message: str = string
    encrypted_message: str = ""

    # Get index of letter, move it by shift amount
    for letter in original_message:
        print(alphabet.index(letter))
        original_index = alphabet.index(letter)

        new_index = original_index + shift_amount

        # If index is greater than len of alphabet, start back at 0 and add from there, not quite right.
        if new_index <= len(alphabet) - 1:
            encrypted_message += alphabet[new_index]
            print(encrypted_message)
        else:
            new_index = 0 + shift_amount
            encrypted_message += alphabet[new_index]
            print(encrypted_message)

    return encrypted_message


def decrypt(string, shift_amount):
    original_message: str = string
    decrypted_message: str = ""

    # Get index of letter, move it by shift amount
    for letter in original_message:
        print(alphabet.index(letter))
        original_index = alphabet.index(letter)

        new_index = original_index - shift_amount

        # If index is greater than len of alphabet, start back at 0 and add from there, not quite right.
        if new_index <= len(alphabet) - 1:
            decrypted_message += alphabet[new_index]
            print(decrypted_message)

    return decrypted_message


if user_choice == "encode":
    encrypt(string=user_string, shift_amount=shift)
elif user_choice == "decode":
    decrypt(string=user_string, shift_amount=shift)
