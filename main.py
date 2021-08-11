import os
import pyttsx3
import speech_recognition as sr
import time
import subprocess
from wsm.sound import Sound
import commands


def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print('Recognizing')

            query = r.recognize_google(audio, language='ru')

            print('The printed query is: {}', query)

        except Exception as e:
            print(e)
            print("Didn't get the query")
            quit()

    return query


def speak(audio):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    try:
        engine.setProperty('voice', voices[0].id)
    except Exception as e:
        engine.setProperty('voice', voices[2].id)

    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    while True:
        command = take_commands().lower()
        if 'гидеон' in command:
            speak('Да? Слушаю Вас.')
            print('Да? Слушаю Вас.')
        if 'выход' in command:
            speak('Приняла, выключаюсь, до скорой встречи!')
            print('Приняла, выключаюсь, до скорой встречи!')
            break
        if 'запусти steam' in command:
            file = 'C:\\Program Files (x86)\\Steam\\Steam.exe'
            os.startfile(file)
            speak('Приняла, включаю Steam, наслаждайтесь!')
            print('Приняла, включаю Steam, наслаждайтесь!')
        if 'добавить команду' in command:
            file = 'main.py'
            # with open(file, 'w'):

            speak('Добавляю команду, ожидайте...')
            time.sleep(3)
            speak('Перегружаюсь...')
            print('Команда добавлена, перезагрузка.')
            subprocess.Popen(["start", "cmd", "/k", "python main.py"], shell=True)
            quit()
        if 'выключить звук' in command:
            Sound.mute()
            print('Выключаю звук, знаю что вы меня не слышите')
        if 'включить звук' in command:
            Sound.mute()
            speak('Надеюсь Вы рады снова меня слышать.')
            print('Надеюсь Вы рады снова меня слышать.')

