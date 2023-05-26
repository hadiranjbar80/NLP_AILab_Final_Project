import modules.speech_recognizer as s
import modules.set_language as sl

if sl.user_choice =='s':
    rec=s.recognizer()
    calculated_text=rec.recognize()
    if rec.error_checker ==False:
        print(f'You said: {calculated_text}')
    else:
        print(calculated_text)
elif sl.user_choice == 't':
    input()
    print('Set your langua')
