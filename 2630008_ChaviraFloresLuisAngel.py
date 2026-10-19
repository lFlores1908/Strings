# COVER PAGE
# Name: Chavira Flores Luis Angel
# Student ID: 2630008
# Group: IM 1-2
# GitHub repository: https://github.com/lFlores1908/Strings

# SUMMARY

# En Python string representa una cadena de caracteres que permite trabajar con
# texto. Las cadenas no se pueden cambiar directamente después de crearlas;
# métodos como lower() y replace() producen una nueva cadena. También es posible
# unir textos con +, medir su tamaño usando len(), obtener fragmentos mediante
# slicing, buscar contenido con in, find() o count(), y sustituir partes con
# replace(). Limpiar los datos de entrada con strip(), lower() o title() ayuda
# a evitar problemas ocasionados por espacios innecesarios o el uso irregular
# de letras mayúsculas y minúsculas.

# GOOD PRACTICES

# - Una cadena no se modifica directamente; las operaciones crean otra.
# - Conviene limpiar el texto con strip() y lower() antes de hacer comparaciones.
# - Explicar el propósito de los índices y fragmentos, como word[0], que obtiene
#   la primera letra de una palabra.
# - Aprovechar los métodos disponibles para trabajar con cadenas.
# - Comprobar primero que el dato tenga contenido y después revisar su formato.
# - Elegir nombres descriptivos y mostrar mensajes fáciles de comprender.

# MAIN

# =============================================================================
# Problem 1: Full name formatter (name + initials)
# =============================================================================
# Description: Reads a full name in a single string, normalizes it (removes
#   extra spaces and fixes upper/lower case) and shows the name in Title Case
#   and the initials (for example: J.C.T.).
#
# Inputs:
#   - full_name (string; full name in upper, lower or mixed case, with
#     possible extra spaces)
#
# Outputs:
#   - "Formatted name: <Name In Title Case>"
#   - "Initials: <X.X.X.>"
#
# Validations:
#   - full_name must not be empty after strip() (a string with only spaces
#     is rejected).
#   - It must contain at least two words (for example, first name and last
#     name), counted with split().
#   - Any error shows "Error: invalid input".
#
# Test cases:
#   1) Normal: "  juan CARLOS   tovar "
#        -> Formatted name: Juan Carlos Tovar / Initials: J.C.T.
#   2) Border: "ana lopez" (exactly two words, the minimum)
#        -> Formatted name: Ana Lopez / Initials: A.L.
#   3) Error: "   " (only spaces) -> Error: invalid input
#      Error: "juan" (only one word) -> Error: invalid input

print("\n--- Problem 1 ---")
MIN_NAME_WORDS = 2

full_name = input("Full name: ").strip()
name_words = full_name.split()

if full_name == "" or len(name_words) < MIN_NAME_WORDS:
    print("Error: invalid input")
else:
    formatted_name = " ".join(name_words).title()

    initials = ""
    for word in name_words:
        initials = initials + word[0].upper() + "."

    print("Formatted name:", formatted_name)
    print("Initials:", initials)


# =============================================================================
# Problem 2: Simple email validator (structure + domain)
# =============================================================================
# Description: Checks whether an email address has a basic correct format:
#   it has exactly one '@', there is at least one '.' after the '@' and it
#   has no blank spaces. If the email is valid, it also shows the domain (the
#   part after '@').
#
# Inputs:
#   - email_text (string)
#
# Outputs:
#   - "Valid email: true" or "Valid email: false"
#   - If valid: "Domain: <domain_part>"
#
# Validations:
#   - email_text must not be empty after strip() (otherwise it shows
#     "Error: invalid input").
#   - The number of '@' is counted with count(); it must be exactly 1.
#   - There must be no spaces inside email_text (" " not in email_text).
#   - Decision: there must be at least one character before the '@'
#     ("@gmail.com" is not valid).
#
# Test cases:
#   1) Normal: "luis@gmail.com"
#        -> Valid email: true / Domain: gmail.com
#   2) Border: "a@b.c" (shortest possible valid email)
#        -> Valid email: true / Domain: b.c
#      Border: "luis@gmail" (no '.' after the '@')
#        -> Valid email: false
#   3) Error: "   " (only spaces) -> Error: invalid input

print("\n--- Problem 2 ---")
email_text = input("Email: ").strip()

if email_text == "":
    print("Error: invalid input")
else:
    at_count = email_text.count("@")
    has_space = " " in email_text
    is_valid_email = False
    domain_part = ""

    if at_count == 1 and not has_space:
        at_position = email_text.find("@")
        domain_part = email_text[at_position + 1:]
        if at_position > 0 and "." in domain_part:
            is_valid_email = True

    print("Valid email:", str(is_valid_email).lower())
    if is_valid_email:
        print("Domain:", domain_part)


# =============================================================================
# Problem 3: Palindrome checker (ignoring spaces and case)
# =============================================================================
# Description: Determines whether a phrase is a palindrome, that is, it reads
#   the same from left to right and from right to left, ignoring spaces and
#   upper/lower case. It also shows the normalized version of the phrase.
#
# Inputs:
#   - phrase (string)
#
# Outputs:
#   - "Normalized phrase:" <phrase without spaces and in lowercase>
#   - "Is palindrome: true" or "Is palindrome: false"
#
# Validations:
#   - phrase must not be empty after strip().
#   - After removing spaces, the phrase must have at least 3 characters.
#   - Any error shows "Error: invalid input".
#
# Test cases:
#   1) Normal: "Anita lava la tina"
#        -> Normalized phrase: anitalavalatina / Is palindrome: true
#      Normal: "Hola mundo"
#        -> Normalized phrase: holamundo / Is palindrome: false
#   2) Border: "aba" (exactly 3 characters, the minimum)
#        -> Normalized phrase: aba / Is palindrome: true
#   3) Error: "   " (only spaces) -> Error: invalid input
#      Error: "a b" (only 2 characters after cleaning) -> Error: invalid input

print("\n--- Problem 3 ---")
MIN_PHRASE_LENGTH = 3

phrase = input("Phrase: ").strip()
normalized_phrase = phrase.lower().replace(" ", "")

if phrase == "" or len(normalized_phrase) < MIN_PHRASE_LENGTH:
    print("Error: invalid input")
else:
    reversed_phrase = normalized_phrase[::-1]
    is_palindrome = (normalized_phrase == reversed_phrase)

    print("Normalized phrase:", normalized_phrase)
    print("Is palindrome:", str(is_palindrome).lower())


# =============================================================================
# Problem 4: Sentence word stats (lengths and first/last word)
# =============================================================================
# Description: Reads a sentence, removes the spaces at the beginning and at
#   the end, splits it into words and shows the number of words, the first
#   word, the last word, the shortest word and the longest word (by length).
#
# Inputs:
#   - sentence (string)
#
# Outputs:
#   - "Word count: <n>"
#   - "First word: <...>"
#   - "Last word: <...>"
#   - "Shortest word: <...>"
#   - "Longest word: <...>"
#
# Validations:
#   - sentence must not be empty after strip().
#   - It must contain at least one word after split().
#   - Decision: if several words have the same length, the first one found
#     is shown.
#
# Test cases:
#   1) Normal: "  the quick brown fox jumps  "
#        -> Word count: 5 / First word: the / Last word: jumps
#           Shortest word: the / Longest word: quick
#   2) Border: "hello" (only one word)
#        -> Word count: 1 / First word: hello / Last word: hello
#           Shortest word: hello / Longest word: hello
#   3) Error: "   " (only spaces) -> Error: invalid input

print("\n--- Problem 4 ---")
sentence = input("Sentence: ").strip()
sentence_words = sentence.split()

if sentence == "" or len(sentence_words) == 0:
    print("Error: invalid input")
else:
    word_count = len(sentence_words)
    first_word = sentence_words[0]
    last_word = sentence_words[-1]

    shortest_word = sentence_words[0]
    longest_word = sentence_words[0]
    for word in sentence_words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print("Word count:", word_count)
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)


# =============================================================================
# Problem 5: Password strength classifier
# =============================================================================
# Description: Classifies a password as "weak", "medium" or "strong". The
#   program goes through the password character by character and uses the
#   boolean flags has_upper, has_lower, has_digit and has_symbol.
#
# Rules used (documented decision):
#   - Strong: length >= 8 and it has an uppercase letter, a lowercase letter,
#     a digit and a symbol (any character that is not a letter or a digit,
#     for example !, @, #).
#   - Medium: length >= 8 and it mixes at least two of the four kinds of
#     characters (but it is not strong).
#   - Weak: everything else (length < 8, or only one kind of character, for
#     example all lowercase or only digits).
#
# Inputs:
#   - password_input (string)
#
# Outputs:
#   - "Password strength: weak"
#   - "Password strength: medium"
#   - "Password strength: strong"
#
# Validations:
#   - The password must not be empty (a password with only spaces is also
#     rejected).
#   - The length is checked with len().
#   - Any error shows "Error: invalid input".
#
# Test cases:
#   1) Normal: "MyPass#2024"
#        -> Password strength: strong
#      Normal: "Password1" (no symbol)
#        -> Password strength: medium
#   2) Border: "Abcd12!x" (exactly 8 characters, all kinds)
#        -> Password strength: strong
#      Border: "Abc12!x" (7 characters, one less than the minimum)
#        -> Password strength: weak
#   3) Error: "" (empty) -> Error: invalid input

print("\n--- Problem 5 ---")
MIN_PASSWORD_LENGTH = 8

password_input = input("Password: ")

if password_input.strip() == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    kinds_count = 0
    if has_upper:
        kinds_count = kinds_count + 1
    if has_lower:
        kinds_count = kinds_count + 1
    if has_digit:
        kinds_count = kinds_count + 1
    if has_symbol:
        kinds_count = kinds_count + 1

    if len(password_input) >= MIN_PASSWORD_LENGTH and kinds_count == 4:
        strength = "strong"
    elif len(password_input) >= MIN_PASSWORD_LENGTH and kinds_count >= 2:
        strength = "medium"
    else:
        strength = "weak"

    print("Password strength:", strength)


# =============================================================================
# Problem 6: Product label formatter (fixed-width text)
# =============================================================================
# Description: Given a product name and its price, it creates a one-line
#   label with the format "Product: <NAME> | Price: $<PRICE>". The complete
#   label must have exactly 30 characters: if it is shorter, spaces are added
#   at the end; if it is longer, it is cut to 30 characters.
#
# Inputs:
#   - product_name (string)
#   - price_text (string; it is converted to a number to validate it and is
#     shown as text in the label)
#
# Outputs:
#   - "Label:" "<exactly 30 characters>" (shown between quotes so the spaces
#     can be seen)
#   - "Length:" <length of the label>
#
# Validations:
#   - product_name must not be empty after strip().
#   - price_text must be convertible to a number (try/except ValueError)
#     and the number must be greater than 0.
#   - Any error shows "Error: invalid input".
#
# Test cases:
#   1) Normal: product "Pen", price "5"
#        -> Label: "Product: Pen | Price: $5      " / Length: 30
#           (the label has 24 characters and 6 spaces are added)
#   2) Border: product "Notebook", price "25" (exactly 30 characters)
#        -> Label: "Product: Notebook | Price: $25" / Length: 30
#      Border: product "Wireless Keyboard", price "49.99" (too long, cut)
#        -> Label: "Product: Wireless Keyboard | P" / Length: 30
#   3) Error: product "   ", price "5" -> Error: invalid input
#      Error: product "Pen", price "abc" -> Error: invalid input
#      Error: product "Pen", price "-5" -> Error: invalid input

print("\n--- Problem 6 ---")
LABEL_LENGTH = 30

product_name = input("Product name: ").strip()
price_text = input("Price: ").strip()

try:
    price_value = float(price_text)
    is_valid = product_name != "" and price_value > 0
except ValueError:
    is_valid = False

if not is_valid:
    print("Error: invalid input")
else:
    label = "Product: " + product_name + " | Price: $" + price_text

    if len(label) > LABEL_LENGTH:
        label = label[:LABEL_LENGTH]
    else:
        label = label + " " * (LABEL_LENGTH - len(label))

    print('Label: "' + label + '"')
    print("Length:", len(label))


# CONCLUSIONS

# Trabajar con cadenas permite recibir, ordenar y presentar la información
# escrita por el usuario. Funciones como strip(), lower(), title(), split() y
# join() ayudan a limpiar y organizar ese contenido. Las comprobaciones previas
# permiten detectar entradas vacías o con un formato que no cumple las reglas.
# En estos ejercicios también se observa que los métodos de strings generan
# nuevas cadenas y que los slices sirven para invertir un texto o limitar su
# longitud. Aplicar estas herramientas hace que el programa sea más claro y
# reduce los errores al procesar texto.
# fácilmente.

# REFERENCES

# References:
# 1) Python documentation - Built-in Types: Text Sequence Type - str.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation - String Methods.
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python Tutorial - An Informal Introduction to Python (strings).
#    https://docs.python.org/3/tutorial/introduction.html
# 4) van Rossum, G., Warsaw, B., Coghlan, A. PEP 8 - Style Guide for Python
#    Code. https://peps.python.org/pep-0008/