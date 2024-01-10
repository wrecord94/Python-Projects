class MorseCodeTranslator:
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                       'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                       '8': '---..', '9': '----.', '0': '-----',
                       ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
                       ')': '-.--.-', ' ': "......."}

    @staticmethod
    def get_key_by_value(value):
        for key, val in MorseCodeTranslator.MORSE_CODE_DICT.items():
            if val == value:
                return key
        return value

    @staticmethod
    def encrypt(text):
        morse_code = ""
        for char in text.upper():
            if char in MorseCodeTranslator.MORSE_CODE_DICT:
                morse_code += (MorseCodeTranslator.MORSE_CODE_DICT[char] + " ")
            else:
                print(f"Ignoring unknown character: {char}")
        return morse_code

    @staticmethod
    def decrypt(morse_code):
        morse_char_list = morse_code.split(" ")
        string_translation = ""
        for char in morse_char_list:
            string_translation += MorseCodeTranslator.get_key_by_value(value=char)
        return string_translation


def main():
    translator = MorseCodeTranslator()

    while True:
        choice = input("Would you like to provide text (encrypt) or Morse code (decrypt)? Type 'exit' to turn off.\n").lower()

        if choice == 'encrypt':
            text_to_encrypt = input("Enter the text to encrypt: ")
            morse_code_translation = translator.encrypt(text_to_encrypt)
            print(morse_code_translation)
        elif choice == 'decrypt':
            morse_code_to_decrypt = input("Enter the Morse code to decrypt: ")
            string_translation = translator.decrypt(morse_code_to_decrypt)
            print(string_translation)
        elif choice == 'exit':
            break


if __name__ == '__main__':
    main()
