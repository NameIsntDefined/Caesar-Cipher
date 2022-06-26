# Caesar Cipher
from colorama import Fore, Style
from time import sleep

print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 'WElCOME TO THE CAESAR CIPHER!\n\n')

direction, language, shift, text = '', '', 0, ''
ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def mistake_proofing():
    global direction, language, shift, text

    while True:
        direction = input(Fore.CYAN + 'Decoding & encoding (d, e):\n').lower()
        if direction not in ('d', 'e'):
            print(Fore.RED + 'Try again!')
        else:
            break

    while True:
        language = input(Fore.CYAN + 'en & ru:\n').lower()
        if language not in ('en', 'ru'):
            print(Fore.RED + 'Try again!')
        else:
            break

    while True:
        try:
            shift = int(input(Fore.CYAN + 'Shift:\n'))
            break
        except ValueError:
            print(Fore.RED + 'InvalidInput!!!\nMust be integer!\nTry again!\n')

    while True:
        text = input('Print the text:\n')
        if not len(text):
            print(Fore.RED + 'The text must not be blank!')
            print('Try again!')
            continue
        break


def select():
    if direction == 'e' and language == 'en':
        print(Fore.CYAN + encoding_decoding_en())

    elif direction == 'e' and language == 'ru':
        print(Fore.CYAN + encoding_decoding_ru())

    elif direction == 'd' and language == 'en':
        print(Fore.CYAN + encoding_decoding_en())

    elif direction == 'd' and language == 'ru':
        print(Fore.CYAN + encoding_decoding_ru())


def encoding_decoding_en():
    encoded_text = ''
    for letter in text:
        if letter.isupper():
            encoded_text += encoding_en_lower_upper_case(letter.lower()).upper()
        elif letter.islower():
            encoded_text += encoding_en_lower_upper_case(letter)
        else:
            encoded_text += letter
    return encoded_text


def encoding_decoding_ru():
    encoded_text = ''
    for letter in text:
        if letter.isupper():
            encoded_text += encoding_ru_lower_upper_case(letter.lower()).upper()
        elif letter.islower():
            encoded_text += encoding_ru_lower_upper_case(letter)
        else:
            encoded_text += letter
    return encoded_text


def encoding_en_lower_upper_case(letter: str) -> str:
    """returns an encoded letter with a certain shift"""
    return chr(((ord(letter) - 97 + shift) % 26) + 97)


def encoding_ru_lower_upper_case(letter):
    return ru_alphabet[(ru_alphabet.find(letter) + shift) % 33]


def repeat():
    while True:
        sleep(1)
        one_more_time = input(Fore.YELLOW + '\nDo you wish to decode & encode something else?:\n').lower()
        if one_more_time in ('да', 'д', 'y', 'yes'):
            mistake_proofing()
            select()
            repeat()
            break
        elif one_more_time in ('no', 'n', 'нет' 'н'):
            print('Come back later!')
            break
        else:
            print("YES: ('да', 'д', 'y', 'yes')")
            print("NO: ('no', 'n', 'нет' 'н')")
            print(Fore.RED + 'Could it be that you meant to speak to an ordinary program as me?')
            sleep(1)


mistake_proofing()
select()
repeat()
