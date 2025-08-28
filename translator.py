import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os


def record_speech():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        st.info(" Listening... Speak now!")
        audio = rec.listen(source, timeout=5, phrase_time_limit=10)
        try:
            text = rec.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error(" Could not understand audio")
        except sr.RequestError as e:
            st.error(f"⚠️ Speech recognition error: {e}")
    return None


def speak_text(text, lang):
    tts = gTTS(text, lang=lang)
    tts.save("output.mp3")
    
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

# Streamlit UI
st.title(" Live Speech Translator")


lang = st.selectbox(
    "Choose target language",
    ["en", "ml", "hi", "fr", "de", "es"],  
    index=1
)


if st.button("🎙️ Speak & Translate"):
    input_text = record_speech()
    if input_text:
        st.write("**You said:**", input_text)
        
        
        translation = GoogleTranslator(source="auto", target=lang).translate(input_text)
        st.success(f"**Translation:** {translation}")
        
        
        speak_text(translation, lang)
