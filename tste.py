from turtle import width
import PySimpleGUI as sg

class TelaMain:
  def __init__(self):
      layout = [
                [sg.Text('V1'), sg.Input(size=(20,200))],
                [sg.Text('V2'), sg.Input()],
                [sg.Button('Enviar Dados')]
      ]
      janela = sg.Window("Dados do Usuário!").layout(layout)
      self.button, self.values = janela.Read()

  def Iniciar(self):
    print(self.values)

tela = TelaMain()
tela.Iniciar()