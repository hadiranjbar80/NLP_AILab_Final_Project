import modules.speech_recognizer as s
import modules.set_language as sl
import modules.translator.Translator as Translator
import modules.translator.constant as constant
import os

input('Enter source language: ')
input("")
input("")

os.system('cls')

if len(sl.get_selected_laguage())!=0:
    target_lang=input('Enter the target language: ')
    user_choice= input('Your text: [(S) for speech or (T) for type): ').lower()
    if user_choice.lower() == 't':
        translator = Translator.Translator()
        os.system('cls')
        print(f'Source language: \nTarget language: {target_lang}')
        while True:
            text=input('Enter your text(Enter Q to quit): ')
            if text=='q':
                break
            print(translator.translate(text, constant.LANGUAGES[target_lang], constant.LANGUAGES[sl.get_selected_laguage()]))
    elif user_choice.lower() =='s':
        translator = Translator.Translator()
        rec=s.recognizer()
        text=calculated_text=rec.recognize()
        print(f"You said {calculated_text}")
        while True:
            if text=='q':
                break
            print(translator.translate(text))

    
