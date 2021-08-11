import os
import subprocess
import time
from main import speak

from wsm.sound import Sound

def commands(command):
    while True:
        if 'гидеон' in command:
            speak('Да? Слушаю Вас.')
            print('Да? Слушаю Вас.')
            commands(command)
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
