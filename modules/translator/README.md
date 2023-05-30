# Translator File
translation module to translate one text in a language to another.

## Translator Class

### Class methods

#### tokenize_words method
This method gets a sentence and returns a list of words in that sentence.

```py
def tokenize_words(self, sentence: str) -> list:
        toekns = nltk.word_tokenize(sentence)
        return toekns
```

#### detect_lang method
This method gets a sentence and detects the language of the given sentence.

```py
def detect_lang(self, sample_sentence: str, defualt_country_code: str="en") -> str:

        DetectorFactory.seed = 0
        try:
            country_code = detect(sample_sentence)
            return country_code
        except:
            return defualt_country_code
```

#### translate method
This method gets a sentence and returns the translated text.

```py
def translate(self, source_sentence: str, target_lang: str='auto', 
                  source_lang: str='auto') -> str:
                  
        translator = google_trans_new.google_translator()
        try:
            translated = translator.translate(source_sentence,
                                            target_lang,
                                            source_lang)
        except:
            translated = "Something went wrong. Please try again later."
        return translated
```

#### translate_words method
This method gets a sentence and a list of translated words in that sentence.

```py
def translate_words(self, word_list: list, target_lang: str='auto', 
                  source_lang: str='auto') -> list:
                  
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
        translated_word_list = translate_words[0]
        tokenized_word_list = translate_words[1]
        for i in range(len(translated_word_list)):
            print(i+1, tokenized_word_list[i] + ":", translated_word_list[i])
```

# google_trans_new File

A free and unlimited python API for google translate.
It's very easy to use and solve the problem that the old api which use tk value cannot be used.
This interface is for academic use only, please do not use it for commercial use.

# constant File

Language and domain constants.
