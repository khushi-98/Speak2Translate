# Speak2Translate


This code consists of two separate Python programs: a speech-to-text converter and a simple text translator.

**Speech-to-Text Converter**

1. The code imports the `speech_recognition` library, which provides functionality for speech recognition.
2. The `speech_to_text()` function is defined, which performs the speech recognition process.
   - It initializes a recognizer object using `sr.Recognizer()`.
   - It captures audio from the microphone using `sr.Microphone()`.
   - It prompts the user to speak and adjusts for ambient noise.
   - It listens for the user's speech and stores the audio data.
   - It attempts to recognize the speech using Google's speech recognition service (`recognizer.recognize_google(audio)`).
   - If the speech is recognized successfully, it returns the text; otherwise, it prints an error message.
3. The `main()` function is defined as the entry point of the program.
   - It prints a welcome message.
   - It enters an infinite loop that waits for the user to press Enter to start recording or type 'exit' to quit.
   - When the user presses Enter, it calls the `speech_to_text()` function and prints the recognized text (if any).
   - If the recording fails, it prints an error message.
4. The code checks if the script is being run as the main program (`if __name__ == "__main__":`) and calls the `main()` function.

**Simple Text Translator**

1. The code imports the `deep_translator` library, which provides functionality for text translation.
2. The `translate_text(text, dest_lang='en')` function is defined, which translates the given text to the specified destination language using the Google Translator engine from the `deep_translator` library.
   - It takes the `text` to be translated and the `dest_lang` (destination language code) as arguments.
   - It returns the translated text.
3. The `main()` function is defined as the entry point of the program.
   - It prints a welcome message.
   - It enters an infinite loop that prompts the user to enter the text to translate or type 'exit' to quit.
   - If the user types 'exit', it prints a goodbye message and exits the loop.
   - Otherwise, it prompts the user to enter the language code to translate to.
   - It calls the `translate_text()` function with the user's input text and the specified destination language code.
   - If the translation is successful, it prints the translated text; otherwise, it prints an error message.
4. The code checks if the script is being run as the main program (`if __name__ == "__main__":`) and calls the `main()` function.

Overall, this code provides a simple command-line interface for converting speech to text using the `speech_recognition` library and translating text to other languages using the `deep_translator` library with Google Translator.
