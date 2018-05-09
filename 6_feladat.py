ALFABET_CODE_TABLE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',

        ' ':'/', '.':'.-.-.-', ',':'--..--',
        ':':'---...', '?':'..--..', "'":'.----.',
        '-':'-....-', '/':'-..-.', '@': '.--.-.',
        '=':'-...-', '(':'-.--.', ')':'-.--.-',
        '+':'.-.-.'
        }

MORSE_CODE_TABLE = dict((v,k) for (k,v) in ALFABET_CODE_TABLE.items())

# morse kódolás
def morsetoalfabet(code):
    alfabet = ''
    temp_char = ''
    for char in code:
        if char==' ' :
            alfabet = alfabet + MORSE_CODE_TABLE[temp_char]
            temp_char = ''
        else:
            temp_char = temp_char + char

    return alfabet


# vissza kódolja a morse kódot, a space-k helyett '/'
def alfabet_to_morse(message):
        encoded_message = ""
        for char in message[:]:
            encoded_message += ALFABET_CODE_TABLE[char.upper()] + " "

        return encoded_message


def main():
    uzenet = input('Üzenet:')

    #for char in uzenet:
    #    print(ALFABET_CODE_TABLE[char.upper()]),

    print('coded ->')
    print(alfabet_to_morse(uzenet))


main()
