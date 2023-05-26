"""
Translator
translation module to translate one text in a language to another.

AI Lab:         Final Project
Date:           May 2023
Author:         Mohammad Javad Rakhshani
"""

# Project imports
import modules.translator.google_trans_new as google_trans_new
import modules.translator.constant

# Python third-party modules
from langdetect import detect
from langdetect import DetectorFactory
import nltk
import time

nltk.download('punkt'); # using the punkt tokenizer
nltk.download('wordnet'); # using the wordNet dictionary

class Translator:
    def __init__(self) -> None:
        pass

    def tokenize_words(self, sentence: str) -> list:
        """
        Sentence word tkenizer to tokenize every word in a sentence.

        Parameters:
        sentence (str): a sentence to tokenize its words.
        """
        toekns = nltk.word_tokenize(sentence)
        return toekns
    
    def detect_lang(self, sample_sentence: str, defualt_country_code: str="en") -> str:
        
        """
        Detect language of a sentence and return 'country-code' of
        the langugage.

        Parameters:
        sample_sentence (str): a sentence to detect its language.
        defualt_country_code="en" (str): default language if not detected.
        """
        DetectorFactory.seed = 0
        try:
            country_code = detect(sample_sentence)
            return country_code
        except:
            return defualt_country_code

    def translate(self, source_sentence: str, target_lang: str='auto', 
                  source_lang: str='auto') -> str:
        """
        Translator method to translate a sentence from a language
        to another.

        Parameters:
        source_sentence (str): a sentence to translate.
        target_lang (str): target traslation language country code.
        source_lang (str): source traslation language country code.
        """
        translator = google_trans_new.google_translator()
        try:
            translated = translator.translate(source_sentence,
                                            target_lang,
                                            source_lang)
        except:
            translated = "Something went wrong. Please try again later."
        return translated
    
    def translate_words(self, word_list: list, target_lang: str='auto', 
                  source_lang: str='auto') -> list:
        """
        Translator method to translate a sentence or word list
        from a language to another.

        Parameters:
        words_or_sentence (list): a list of words in a sentence or
        a sentence to be tokenized.
        target_lang (str): target traslation language country code.
        source_lang (str): source traslation language country code.
        """
        translator = google_trans_new.google_translator()
        tokenized_word_list = self.tokenize_words(word_list)
        translated_word_list = []
        for word in tokenized_word_list:
            translated_word_list.append(translator.translate(word,
                                                             target_lang,
                                                             source_lang))
            time.sleep(1.5) # Delay to prevent spam detectors
        
        return [translated_word_list, tokenized_word_list]
    
    def print_word_translation(self, translate_words: list) -> None:
        """
        Print every word and its translation in a sentence.

        Parameters:
        translate_words (list): a list of 'translate_words()' method
        return value.
        """
        translated_word_list = translate_words[0]
        tokenized_word_list = translate_words[1]
        for i in range(len(translated_word_list)):
            print(i+1, tokenized_word_list[i] + ":", translated_word_list[i])
        

t = Translator()

print(t.translate("Hello world"))