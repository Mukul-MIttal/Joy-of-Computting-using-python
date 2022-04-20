
import speech_recognition as SR
Audio_File=("Audio.wav")
r=SR.Recognizer()
with SR.AudioFile(Audio_File) as source:
    audio=r.record(source)
try:
    print("audio file contains "+ r.recognize_google(audio))
except SR.UnknownValueError:
    print("somethimg went wrong please try another audio.")
except SR.RequestError:
    print("Couldn't get the result from speach recognisation.")