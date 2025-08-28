
import speech_recognition as sr
from deep_translator import GoogleTranslator
import pyttsx3
from gtts import gTTS
import os

def speak_text(text, lang="en"):
    if lang == "en":
        # Use pyttsx3 (offline)
        speaker = pyttsx3.init()
        speaker.setProperty('rate', 150)
        speaker.say(text)
        speaker.runAndWait()
    else:
        
        tts = gTTS(text, lang=lang)
        tts.save("output.mp3")
        os.system("start output.mp3")  

def main():
    rec = sr.Recognizer()
    
    target_lang = input("Enter target language code(en=English,ml=Malayalam,fr=French,hi=Hindi:")
    
    translator = GoogleTranslator(source='auto', target=target_lang)
    
    print("\nSpeak......")
    
    while True:
        try:
            with sr.Microphone() as source:
                rec.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = rec.listen(source, timeout=5, phrase_time_limit=10)
                print("Analyzing...")
                text = rec.recognize_google(audio)
                print("You said:", text)
                
                # Translate
                translation = translator.translate(text)
                print("Translation:", translation)
                
                # Speak translation (auto choose engine)
                speak_text(translation, target_lang)
                
                print("\nSpeak again.....")

        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    main()
