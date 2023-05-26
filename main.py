import modules.speech_recognizer as s

user_choice= input('Which do you choose to enter your text "Speech or Entering a Text"(s/t)?')

if user_choice.lower() =='s':
    rec=s.recognizer()
    calculated_text=rec.recognize()
    print(f"You said {calculated_text}")
elif user_choice.lower() == 't':
    givin_text=input('Enter your text\n')
    print(givin_text)