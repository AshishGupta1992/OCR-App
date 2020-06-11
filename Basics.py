import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
#sr.recognize_google()

#recognizing audio file
#harvard = sr.AudioFile('harvard.wav')
#with harvard as source:
#    r.adjust_for_ambient_noise(source)
#    audio = r.record(source)

#print(r.recognize_google(audio))

#Using mIke

mic = sr.Microphone()

with mic as source:
    audio = r.listen(source)

print(r.recognize_google(audio))
