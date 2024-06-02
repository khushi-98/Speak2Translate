# import speech_recognition as sr

# def speech_to_text():
#     # Initialize recognizer
#     recognizer = sr.Recognizer()

#     # Capture audio from microphone
#     with sr.Microphone() as source:
#         print("Please speak:")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#         audio = recognizer.listen(source)

#     # Convert speech to text
#     try:
#         print("Recognizing...")
#         text = recognizer.recognize_google(audio)
#         return text
#     except sr.UnknownValueError:
#         print("Sorry, could not understand audio.")
#     except sr.RequestError as e:
#         print("Request failed; {0}".format(e))

# def main():
#     print("Welcome to the Speech to Text Converter!")

#     while True:
#         input("Press Enter to start recording (or type 'exit' to quit): ")
#         text = speech_to_text()
#         if text:
#             print("You said:", text)
#         else:
#             print("Recording failed.")

# if __name__ == "__main__":
#     main()



# from deep_translator import GoogleTranslator

# def translate_text(text, dest_lang='en'):
#     translated_text = GoogleTranslator(source='auto', target=dest_lang).translate(text)
#     return translated_text

# def main():
#     print("Welcome to the Simple Translator!")

#     while True:
#         source_text = input("Enter the text to translate (or type 'exit' to quit): ")
#         if source_text.lower() == 'exit':
#             print("Exiting the translator. Goodbye!")
#             break

#         dest_lang = input("Enter the language code to translate to (e.g., 'fr' for French): ")

#         try:
#             translated_text = translate_text(source_text, dest_lang)
#             print("Translated text:", translated_text)
#         except Exception as e:
#             print("Translation failed:", e)

# if __name__ == "__main__":
#     main()



# import pyttsx3

# text_speech=pyttsx3.init()


# answer=input("Enter the text:-")
# text_speech.say(answer)
# text_speech.runAndWait()




# import speech_recognition as sr
# from deep_translator import GoogleTranslator
# import pyttsx3

# def speech_to_text():
#     # Initialize recognizer
#     recognizer = sr.Recognizer()

#     # Capture audio from microphone
#     with sr.Microphone() as source:
#         print("Please speak:")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#         audio = recognizer.listen(source)

#     # Convert speech to text
#     try:
#         print("Recognizing...")
#         text = recognizer.recognize_google(audio)
#         return text
#     except sr.UnknownValueError:
#         print("Sorry, could not understand audio.")
#         return None
#     except sr.RequestError as e:
#         print("Request failed; {0}".format(e))
#         return None

# def translate_text(text, dest_lang='en'):
#     translated_text = GoogleTranslator(source='auto', target=dest_lang).translate(text)
#     return translated_text

# def text_to_speech(text):
#     speech_engine = pyttsx3.init()
#     speech_engine.say(text)
#     speech_engine.runAndWait()

# def main():
#     print("Welcome to the Speech to Text Translator!")

#     while True:
#         input("Press Enter to start recording (or type 'exit' to quit): ")
#         source_text = speech_to_text()
#         if source_text:
#             print("You said:", source_text)
#             dest_lang = input("Enter the language code to translate to (e.g., 'fr' for French): ")
#             translated_text = translate_text(source_text, dest_lang)
#             print("Translated text:", translated_text)
#             text_to_speech(translated_text)
#         else:
#             print("Recording failed.")

# if __name__ == "__main__":
#     main()





# import speech_recognition as sr
# from deep_translator import GoogleTranslator
# import pyttsx3

# def speech_to_text():
#     # Initialize recognizer
#     recognizer = sr.Recognizer()

#     # Capture audio from microphone
#     with sr.Microphone() as source:
#         print("Please speak:")
#         recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
#         try:
#             audio = recognizer.listen(source, timeout=5)  # Set timeout for capturing audio
#             print("Audio captured.")
#             return recognizer.recognize_google(audio)
#         except sr.WaitTimeoutError:
#             print("Timeout occurred. No speech detected.")
#             return None
#         except sr.UnknownValueError:
#             print("Sorry, could not understand audio.")
#             return None
#         except sr.RequestError as e:
#             print("Request failed; {0}".format(e))
#             return None

# def translate_text(text, dest_lang='en'):
#     translated_text = GoogleTranslator(source='auto', target=dest_lang).translate(text)
#     return translated_text

# def text_to_speech(text):
#     speech_engine = pyttsx3.init()
#     speech_engine.say(text)
#     speech_engine.runAndWait()

# def main():
#     print("Welcome to the Speech to Text Translator!")

#     while True:
#         input("Press Enter to start recording (or type 'exit' to quit): ")
#         source_text = speech_to_text()
#         if source_text:
#             print("You said:", source_text)
#             dest_lang = input("Enter the language code to translate to (e.g., 'fr' for French): ")
#             translated_text = translate_text(source_text, dest_lang)
#             print("Translated text:", translated_text)
#             text_to_speech(translated_text)
#         else:
#             print("Recording failed.")

# if __name__ == "__main__":
#     main()

# import speech_recognition as sr
# from deep_translator import GoogleTranslator
# import pyttsx3

# def speech_to_text():
#     # Initialize recognizer
#     recognizer = sr.Recognizer()

#     # Capture audio from microphone
#     with sr.Microphone() as source:
#         print("Please speak:")
#         recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
#         try:
#             audio = recognizer.listen(source, timeout=5)  # Set timeout for capturing audio
#             print("Audio captured.")
#             return recognizer.recognize_google(audio)
#         except sr.WaitTimeoutError:
#             print("Timeout occurred. No speech detected.")
#             return None
#         except sr.UnknownValueError:
#             print("Sorry, could not understand audio.")
#             return None
#         except sr.RequestError as e:
#             print("Request failed; {0}".format(e))
#             return None

# def translate_text(text, dest_lang='en'):
#     translated_text = GoogleTranslator(source='auto', target=dest_lang).translate(text)
#     return translated_text

# def text_to_speech(text):
#     speech_engine = pyttsx3.init()
#     speech_engine.say(text)
#     speech_engine.runAndWait()

# def main():
#     print("Welcome to the Speech to Text Translator!")

#     # Start one loop
#     input("Press Enter to start recording: ")
#     source_text = speech_to_text()
#     if source_text:
#         print("You said:", source_text)
#         dest_lang = input("Enter the language code to translate to (e.g., 'fr' for French): ")
#         translated_text = translate_text(source_text, dest_lang)
#         print("Translated text:", translated_text)
#         text_to_speech(translated_text)
#     else:
#         print("Recording failed.")

# if __name__ == "__main__":
#     main()



import speech_recognition as sr
from deep_translator import GoogleTranslator
import pyttsx3

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture audio from microphone
    with sr.Microphone() as source:
        print("Please speak:")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=5)  # Set timeout for capturing audio
            print("Audio captured.")
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("Timeout occurred. No speech detected.")
            return None
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return None
        except sr.RequestError as e:
            print("Request failed; {0}".format(e))
            return None

def translate_text(text, dest_lang='en'):
    translated_text = GoogleTranslator(source='auto', target=dest_lang).translate(text)
    return translated_text

def text_to_speech(text):
    speech_engine = pyttsx3.init()
    speech_engine.say(text)
    speech_engine.runAndWait()

def main():
    print("Welcome to the Speech to Text Translator!")

    # Capture audio and process it
    source_text = speech_to_text()
    if source_text:
        print("You said:", source_text)
        dest_lang = input("Enter the language code to translate to (e.g., 'fr' for French): ")
        translated_text = translate_text(source_text, dest_lang)
        print("Translated text:", translated_text)
        text_to_speech(translated_text)
    else:
        print("Recording failed.")

if __name__ == "__main__":
    main()
