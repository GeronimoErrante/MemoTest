import PySimpleGUI as sg
from src.windows import menu
from src.handlers import lol
from src.handlers import art

def start():
    window = loop()
    window.close

def loop():
    window = menu.build()
    while True:
        event, _values = window.read()
        if event in ('-CLOSE-', sg.WIN_CLOSED):
            break
        if event == ('-BANS-'):
            lol.calcularLol()
        if event == ('-ARTS-'):
            art.calcularArtistas()

    return window