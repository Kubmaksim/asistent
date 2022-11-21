import pyttsx3
import os,random 
import datetime


class _TTS:
    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()

    def start(self, text_):
        
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
        self.engine.say(text_)
        self.engine.runAndWait()

x = input("Enter please:")
tts = _TTS()
tts.start(x)


class Functional:

    def datetime():
        day = datetime.datetime.now()
        look = 'Сегодня {0:%d}  число.\n  Сейчас  {0:%H}  часов и {0:%M} минуты'.format(day)
        return tts.start(look)
    def telegram():
        return os.system('open /Applications/Telegram.app')

    def google():
        return os.system('/Applications/Google Chrome.app')
    
    def book():#prob
        with open('file_name.txt', 'r') as f:
            for i in f.l:
                x = i
        return tts.start(x)
    
    def fyni():
        list = ['Финал  сказки  о    Рыбаке  и  Золотой   рыбке  —  это  возвращение  к  заводским  настройкам.',
                'Библиотекарша  устроилась   на работу   в   бордель. Теперь  у   каждой   девочки  в  карточке  четко  написано,  кто  ее  брал  и  когда.',
                'Только  в  американских  фильмах  20-ти  летняя  блондинка  с  четвертым  размером  груди  может  быть  специалистом  по  ядерному  оружию.',
                'Джинн:  —  Я  исполню  любое  твое  желание,  но  у  твоего  врага  будет  вдвое  больше.  Что  же  ты  хочешь? —   Давление  120  на  80.'
        ]
        random_id = random.randrange(len(list))
        return tts.start(list[random_id])
    





if x.lower() == 'телеграм' or x.lower() == 'открыть телеграм':
    tts.start('Открываю телеграм')
    Functional.telegram()
elif x.lower() == 'браузер' or x.lower() == 'открыть браузер':
    tts.start('Браузер открыт!')
    Functional.google()
elif x.lower() == 'книги' or x.lower() == 'открыть книги':
    Functional.book()
elif x.lower() == 'что ты можешь' or x.lower() == 'покажи свои возможности':
    tts.start('Я умею открывать приложения на твоем компьютере')
elif x.lower() == 'анекдот' or x.lower() == 'расскажи анекдот':
    Functional.fyni()
elif x.lower() == 'date':
    Functional.datetime()
else:
    tts.start('Не понимаю')
    


