"""
Gets a speech from user microphone and convert the speech to text for translation.

Data Mining:    Final Project
Date:           May 2023
Author:         Mohammed Hadi Ranjbar
"""

import speech_recognition as sr

class recognizer:
    def recognize(self):

        r=sr.Recognizer()

        with sr.Microphone() as source:                                                                       
            print('Speak: ')
            audio=r.listen(source)

        try:
           return r.recognize_google(audio)
        except sr.UnknownValueError:
            return 'Could not understand audio'
        except sr.RequestError as e:
            return f'Could not request results: {0}'.format(e)