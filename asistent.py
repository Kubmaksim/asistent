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

    def telegram():
        return os.system('open /Applications/Telegram.app')

    def google():
        return os.system('/Applications/Google Chrome.app')
    
    def book():
        return os.system('open /System/Applications/Books.app')




if x.lower() == 'телеграм' or x.lower() == 'открыть телеграм':
    tts.start('Открываю телеграм')
    Functional.telegram()
elif x.lower() == 'браузер' or x.lower() == 'открыть браузер':
    tts.start('Браузер открыт!')
    Functional.google()
elif x.lower() == 'книги' or x.lower() == 'открыть книги':
    tts.start('Приятного чтения')
    Functional.book()
elif x.lower() == 'что ты можешь' or x.lower() == 'покажи свои возможности':
    tts.start('Я умею открывать приложения на твоем компьютере')
    
else:
    tts.start('Не понимаю')
    


