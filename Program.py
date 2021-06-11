from os import close
from tkinter import Event
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, FileBrowse, FolderBrowse

class ScreenPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Digite o nome do Arquivo ou Procure no Browser', key='arquivo',auto_size_text=True, justification='rigth'),      
             sg.InputText('Selecione o arquivo'), sg.FileBrowse()],

            [sg.Text('Diretorio de Origem', auto_size_text=True, justification='rigth'),      
             sg.InputText('Selecione um diretorio', key='dir_1'), sg.FolderBrowse()],

            [sg.Text('Diretorio de Destino', key='dir_2', auto_size_text=True, justification='rigth'),
            sg.InputText('Selecionar diretorio'), sg.FolderBrowse()],

            [sg.Button('Start', key='start'),sg.Button('Closed', key='closed')]
        ]
        #Janela
        self.janela = sg.Window("Transfere.ae!").layout(layout)
        



    #Extrair os dados da tela
    def Iniciar(self):
        while True:    
            self.button, self.values = self.janela.Read()
            arquivo = self.values['arquivo']
            dir_1 = self.values['dir_1']
            dir_2 = self.values['dir_2']
            
            print(self.values)
    
tela = ScreenPython()
tela.Iniciar()
        

