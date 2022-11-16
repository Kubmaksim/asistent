import pyttsx3
import os


class _TTS:
    engine = None

    def __init__(self):
        self.engine = pyttsx3.init()

    def start(self, text_):
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0') # Вот сюда пихай адрес голоса, в кавычках.
        self.engine.say(text_)
        self.engine.runAndWait()


# и вызываем:
x = input("Enter please:")
tts = _TTS()
tts.start(x)

class Functional:
    def app():
        return os.system('open /Applications/Telegram.app')



    
if x == 'Телеграм':
    tts.start('Открываю телеграм')
    Functional.app()
else:
    print('No undenstend')


