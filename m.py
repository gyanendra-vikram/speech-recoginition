# import googletrans
# import speech_recognition as sr

# r = sr.Recognizer()

# text = ""

# with sr.AudioFile("audio.wav") as source:
#     r.adjust_for_ambient_noise(source)
#     a = r.listen(source)
#     text = r.recognize_google(a)
#     print("Converting Sound To Your Fuckin Audio...")
#     print(text)

# def convertlang(text, frm, to):
#     print("Text To Be Translated : " + text)
#     translator = googletrans.Translator()
#     text_to_translate = translator.translate(text, src=frm, dest=to)
#     text = text_to_translate.text
#     return text

# convertlang(text, "en", "hi")
# convertlang(text, "en", "hi")

import sounddevice as sd
#from scipy.io.wavfile import write
import wavio
def record_audio():
    print("Setting Value Of FS To 44100 ......")
    fs = 44100
    print("Max Audio Duration Allowed Is 6 Seconds .....")
    seconds = 6 
    print("Recording ......")
    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    print("Writing File To audio.wav .....")
    #write("audio.wav", fs, my_recording)
    wavio.write("audio.wav", my_recording, fs, sampwidth=3)
    print("File Saved As audio.wav ......")
    return 0


import speech_recognition as sr
def recognise_audio(audioFilename, lang):
    print(f"Recognisation Process Started For {audioFilename} ......")
    print("Initialising Recogniser ......")
    recogniser = sr.Recognizer()
    with sr.AudioFile(audioFilename) as source:
        print("Cleaning Audio For Good Results ......")
        recogniser.adjust_for_ambient_noise(source)
        print("Listening To Source ......")
        audio = recogniser.listen(source)
    print("Recognising Source ......")
    audio_text = recogniser.recognize_google(audio, language=lang)
    print("Recognisation Of Source Successful ......")
    print(f"Text :: {audio_text}")
    return audio_text

# from translate import Translator
# def convert_lang(text, to):
#     print("Translation Service Started ......")
#     translator = Translator(to_lang="en")
#     print("Translating Text ......")
#     print(text)
#     try:
#         converted_data = translator.translate(text)
#     except AttributeError:
#         print("Attribute Error !")
#         print("Retrying...")
#         convert_lang(text, to_lang)
#     print("Text Translated Successfully ......")
#     # converted_data = converted_data.decode("utf-8")
#     print(f"Converted Text :: {converted_data}")
#     return converted_data

import os
import subprocess
def convert_lang(text, frm, to):
    converted_lang = subprocess.check_output("translate-cli -f {} -t {} '{}' -o".format(frm, to, text), shell=True)
#    converted_lang = converted_lang.decode("utf-8")
    print(converted_lang)
    return converted_lang

import pyttsx3
def sayData(pronunciation):
    print("Speaking Engine Starting .....")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    print("Speaking Engine Started Successfully .....")
    print(f"Speaking :: {pronunciation}")
    engine.say(pronunciation)
    engine.runAndWait()
    print("Successful .....")
    return 0

# from gtts import gTTS
# def convert_lang_to_audio(pronunciation, to):
#     tts = gTTS(text=pronunciation, lang=to)
#     tts.save("converted_text.mp3")
#     print("File saved!")






def INIT():
    type = int(input("Type 1 For Custom File 2 To Record The Audio Then Press Enter > "))
    lang = input("Select Input Language > ")
    if type == 1:
        choice = input("Enter Audio File Name (*.wav)(English Audio Data) For Conversion :: ")
    elif type == 2:
        record_audio()
        choice = "audio.wav"

    #choice = input("Enter Audio File Name (*.wav)(English Audio Data) For Conversion :: ")
    audio_text = recognise_audio(choice, lang)
    frm = input("Enter Input Language :: ")
    to = input("Enter Output Language :: ")
    pronunciation = convert_lang(audio_text, frm, to)
    sayData(pronunciation)
    # convert_lang_to_audio(pronunciation, to)

if __name__ == "__main__":
    INIT()
# text = convert_lang("This Is", "hi")
# print("Pronunciation")
# print(text)










