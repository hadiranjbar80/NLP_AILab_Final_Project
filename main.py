import modules.speech_recognizer as s

user_choice= input('Your text: [(S) for speech or (T) for type)').lower()

if user_choice.lower() =='s':
    rec=s.recognizer()
    calculated_text=rec.recognize()
    print(f"You said {calculated_text}")
elif user_choice.lower() == 't':
    givin_text=input('Enter your text\n')
    print(givin_text)