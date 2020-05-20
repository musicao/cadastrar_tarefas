import re

regex = re.compile(r'[\n\r\t]')
NONDIGIT = re.compile(r'[^0-9]')



def limpar(tela):
    return regex.sub("", tela)