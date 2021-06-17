from os import close
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, FileBrowse, FolderBrowse, WINDOW_CLOSED
import shutil, errno
    
def Mover(src, dst):
    try:
        shutil.move(src, dst)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            print('Directory not copied. Error: %s' % e) 

class ScreenPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Digite o nome do Arquivo ou Procure no Browser', key='arquivo',auto_size_text=True, justification='rigth'),      
             sg.InputText('Selecione o arquivo'), sg.FileBrowse()],

            [sg.Text('Diretorio de Origem', auto_size_text=True, justification='rigth'),      
             sg.InputText('Selecione um diretorio', key='src'), sg.FolderBrowse()],

            [sg.Text('Diretorio de Destino', key='dst', auto_size_text=True, justification='rigth'),
            sg.InputText('Selecionar diretorio'), sg.FolderBrowse()],

            [sg.Button('Start', key='start'),sg.Button('Closed', key='closed')]
        ]
        #Janela
        self.janela = sg.Window("Transfere.ae!", layout)

        #Extrair os dados da tela
    def Iniciar(self):
        while True: 
            evento, values = self.janela.read()
            if evento == WINDOW_CLOSED:
                break
            if evento == 'start':
                Mover(values[0], values[1])
                print("Arquivos foram transferidos")
            
tela = ScreenPython()
tela.Iniciar()
        

