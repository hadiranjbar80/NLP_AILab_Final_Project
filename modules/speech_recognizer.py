"""
Gets a speech from user microphone and convert the speech to text for translation.

AI:             Final Project
Date:           May 2023
Author:         Mohammed Hadi Ranjbar
"""

import speech_recognition as sr

class recognizer:
    """
    error_checker: If there would be an error this variable would be True otherwise False
    """

    error_checker=False
    def recognize(self):
        
        r=sr.Recognizer()
    
        with sr.Microphone() as source:                                                                       
            print('Speak: ')
            audio=r.listen(source)

        try:
           return r.recognize_google(audio)
        except sr.UnknownValueError:
            error_checker=True
            return 'Could not understand audio'
        except sr.RequestError as e:
            error_checker=True
            return f'Could not request results: {0}'.format(e)