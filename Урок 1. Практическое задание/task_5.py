"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!
"""


import subprocess
import chardet

def ping(domain):
    args = ['ping', domain]

    ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in ping.stdout:
        char_detect = chardet.detect(line)
        print(line.decode(char_detect['encoding']))

# ping('yandex.ru')
ping('youtube.com')