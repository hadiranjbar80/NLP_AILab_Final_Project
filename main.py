import modules.speech_recognizer as s
import modules.set_language as sl

if sl.user_choice.lower() =='s':
    rec=s.recognizer()
    calculated_text=rec.recognize()
    print(f"You said {calculated_text}")
elif sl.user_choice.lower() == 't':
    givin_text=input('Enter your text\n')
    print(givin_text)