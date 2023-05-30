## set_language file

### Valriables

#### allowd 
A list of **allowed** characters that user can type.

#### typed_char
A list of characters that user types.

#### integreated_char
This is a string variable that consists of integrated **typed characters**.

#### languages
A list of languages.

#### possible_choises
A list of choises that user can have filtered by **typed_char** list.

#### _source_language
The language that the user wants to enter his/her text.

#### _target_language
Translate language.(The language that user wants to see the result with).

### File Methods

#### get_language_list Method

Prints all languages for user

```py
def get_language_list():
    for i in range(len(languages)):
        print(i, str(languages[i]).title())
```

#### gte_source_language Method
This method returns the country code of the source language, if the given language would not be found it returns **en**.

```py
def get_source_laguage():
    index = -1
    for i in lang_constants.LANGUAGES.values():
        index += 1
        if i == _source_language:
            return list(lang_constants.LANGUAGES.keys())[index]
    return "en"
```

#### get_target_language Method
This method returns the country code of the target language, if the given language would not be found it returns **en**

```py
def get_target_laguage():
    index = -1
    for i in lang_constants.LANGUAGES.values():
        index += 1
        if i == _target_language:
            return list(lang_constants.LANGUAGES.keys())[index]
    return "en"
```

#### set_source_language Method
This method sets(by hitting enter) the selected language into **_source_language** variable.

```py
def set_source_language(key):
    global typed_char
    global integreated_char
    global l1
    global possible_choise
    global _source_language
    
    integreated_char = ""
    if key.name=='backspace':
        if len(typed_char) > 0:
            typed_char.pop()
            integreated_char=integreated_char[:-1]
    elif key.name.lower() in allowd:
        typed_char.append(key.name)

    elif key.name == 'enter':
        typed_char = []
        keyboard.unhook_all()
        _source_language= possible_choise[0]
        

    for char in typed_char:
        os.system("cls")
        integreated_char += char
        possible_choise = [lang for lang in languages if lang.startswith(integreated_char)]
```

#### set_target_language Method
This method sets the selected target language into **_target_language** variable.

```py
def set_target_language(key):
    global typed_char
    global integreated_char
    global l1
    global possible_choise
    global _target_language
    
    integreated_char = ""
    if key.name=='backspace':
        if len(typed_char) > 0:
            typed_char.pop()
            integreated_char=integreated_char[:-1]
    elif key.name.lower() in allowd:
        typed_char.append(key.name)

    elif key.name == 'enter':
        typed_char = []
        keyboard.unhook_all()
        _target_language= possible_choise[0]
        

    for char in typed_char:
        os.system("cls")
        integreated_char += char
        possible_choise = [lang for lang in languages if lang.startswith(integreated_char)]

    
    print("Choises:")
    print(f'Typed language: {integreated_char}')
    for i in range(len(possible_choise)):
        print(i+1, "-", possible_choise[i])
```
