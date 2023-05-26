"""
Determines which languages should use choose.
User types a query and it returns languages that match the query (User can pick one of the returned languages).

AI:             Final Project
Date:           May 2023
Author:         Mohammed Hadi Ranjbar
"""

import keyboard
import os

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
l1=["persian", "pashto", "persa","english","french"]
possible_choise = []

# Prints list of languages for use
def get_language_list():
    for i in range(len(l1)):
        print(i, l1[i])

#
def set_language(key):
    global typed_char
    global integreated_char
    global l1
    global possible_choise
    
    integreated_char = ""
    os.system("cls")
    if key.name=='backspace':
        if len(typed_char) > 0:
            typed_char.pop()
            integreated_char=integreated_char[:-1]
    elif key.name.lower() in allowd:
        typed_char.append(key.name)

    for char in typed_char:
        integreated_char += char
        possible_choise = [lang for lang in l1 if lang.startswith(integreated_char)]

    
    print("Choises:")
    print(f'Typed language: {integreated_char}')
    for i in range(len(possible_choise)):
        print(i+1, "-", possible_choise[i])

user_choice = input('Which do you choose to enter your text "Speech or Entering a Text"(s/t)?').lower()

get_language_list()

keyboard.on_press(callback=set_language)