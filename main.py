import modules.speech_recognizer as s
import modules.set_language as sl

if sl.user_choice =='s':
user_choice= input('Your text: [(S) for speech or (T) for type)').lower()

if sl.user_choice.lower() =='s':
    rec=s.recognizer()
    calculated_text=rec.recognize()
    if rec.error_checker ==False:
        print(f'You said: {calculated_text}')
    else:
        print(calculated_text)
elif sl.user_choice == 't':
    input()
    print('Set your langua')
