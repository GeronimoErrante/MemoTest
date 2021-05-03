import PySimpleGUI as sg

def build():
    color_fondo = "#148515"
    fuente = ('Arial',10)
    ventana = {'size':(300,250), 'background_color':color_fondo, 'element_justification':'center'}
    botones = {'size':(20,2), 'button_color':'#000000','font':fuente,'border_width':3,'focus':True}
    titulos = {'font':('Arial Black',15), 'background_color':color_fondo, 'text_color':'#ffffff'}

    # Layout
    layout = [
                [sg.Text(k='-TITULO-', text='Datos a analizar', **titulos)],     
                [sg.Button(k='-BANS-', button_text= 'Top 10 bans de league of legends', **botones)], 
                [sg.Button(k='-ARTS-', button_text= 'Top 10 canciones más populares de Spotify', **botones)],         
                [sg.Button(k='-CLOSE-', button_text='Salir', pad=((0,0),(25,0)),**botones)]               
            ]

    window = sg.Window('Menu',layout,**ventana)
    return window