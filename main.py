import modules.speech_recognizer as s
import modules.set_language as sl
import modules.translator.Translator as Translator
import modules.translator.constant as constant
import os


sl.keyboard.on_press(callback=sl.set_source_language)

input('Enter source language: ')


input("Next ->")

sl.keyboard.on_press(callback=sl.set_target_language)
input('Enter target language: ')

if len(sl.get_source_laguage())!=0 and len(sl.get_target_laguage())!=0:
    user_choice= input('Your text: [(S) for speech or (T) for type): ').lower()
    if user_choice.lower() == 't':
        translator = Translator.Translator()
        while True:
            text=input(f'Translate [{constant.LANGUAGES[sl.get_source_laguage()].title()} -> {constant.LANGUAGES[sl.get_target_laguage()].title()}] (Enter Q to quit): ')
            if text=='q':
                break
            print(translator.translate(text, sl.get_target_laguage(),
                                       sl.get_source_laguage()))
    elif user_choice.lower() =='s':
        translator = Translator.Translator()
        rec=s.recognizer()
        while True:
            text=rec.recognize()
            if text=='q':
                break
        
            print(translator.translate(text, sl.get_target_laguage(),
                                        sl.get_source_laguage()))

    
