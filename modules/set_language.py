"""
Determines which languages should use choose.
User types a query and it returns languages that match the query (User can pick one of the returned languages).

AI:             Final Project
Date:           May 2023
Author:         Mohammed Hadi Ranjbar
"""

import keyboard
import os
import modules.translator.constant as lang_constants

allowd = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
  'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
  'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
  'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M',
  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
  'W', 'X', 'Y', 'Z'
]

typed_char=[]
integreated_char = ""
languages=list(lang_constants.LANGUAGES.values())
possible_choise = []
_selected_language=''
# Prints list of languages for use
def get_language_list():
    for i in range(len(languages)):
        print(i, str(languages[i]).title())

def get_selected_laguage():
    index = -1
    for i in lang_constants.LANGUAGES.values():
        index += 1
        if i == _selected_language:
            return list(lang_constants.LANGUAGES.keys())[index]
    return "en"

def set_language(key):
    global typed_char
    global integreated_char
    global l1
    global possible_choise
    global _selected_language
    
    integreated_char = ""
    os.system("cls")
    if key.name=='backspace':
        if len(typed_char) > 0:
            typed_char.pop()
            integreated_char=integreated_char[:-1]
    elif key.name.lower() in allowd:
        typed_char.append(key.name)

    elif key.name == 'enter':
        _selected_language= possible_choise[0]
        keyboard.unhook_all()
        

    for char in typed_char:
        integreated_char += char
        possible_choise = [lang for lang in languages if lang.startswith(integreated_char)]

    
    print("Choises:")
    print(f'Typed language: {integreated_char}')
    for i in range(len(possible_choise)):
        print(i+1, "-", possible_choise[i])

    # if key.name == 'enter':
    #     os.system("cls")
    #     keyboard.unhook_all()

get_language_list()

keyboard.on_press(callback=set_language)