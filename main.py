import modules.speech_recognizer as s
import modules.set_language as sl
import modules.translator.Translator as Translator
import modules.translator.constant as constant


sl.keyboard.on_press(callback=sl.set_source_language)

input('Enter language: ')


input("Next ->")

sl.keyboard.on_press(callback=sl.set_target_language)
input('Enter language: ')


print("Source:", sl.get_source_laguage(), "Target:", sl.get_target_laguage())

if len(sl.get_source_laguage())!=0 and len(sl.get_target_laguage())!=0:
    user_choice= input('Your text: [(S) for speech or (T) for type): ').lower()
    if user_choice.lower() == 't':
        translator = Translator.Translator()
        print(sl.get_selected_laguage())
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

    
