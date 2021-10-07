from tkinter.constants import FALSE, TRUE
import PySimpleGUI as sg
from QrcodeGen import QrcodeGen as QR


class QrcodeGui:
    def __init__(self):
        sg.theme("SystemDefault")
        font = ("verdana, 12")
        layout = [
            [sg.T("")], [sg.Text("Escolha o Arquivo:", font=font, size=(15, 1)), sg.Input(
                key="caminho", enable_events=True), sg.FileBrowse()],
            [sg.Text("Escolha a Coluna:", font=font, size=(15, 1)), sg.Input(
                key="coluna", size=(30, 1))],
            [sg.Text("Nome do Diretório:", font=font, size=(15, 1)), sg.Input(
                key="diretorio", size=(30, 1))],
            [sg.Text("Colunas da Planilha:", font=font,
                     size=(15, 1)), sg.Output()],
            [sg.Button("Enviar dados", font=font)]
        ]

        self.janela = sg.Window("Gerador de QrCode", layout,
                                size=(600, 230), auto_size_buttons=True, resizable=False,
                                auto_size_text=True)

    def iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
            if self.event == "caminho":
                dados = QR.carregarColunas(self.values['caminho'])
                for x in dados:
                    print(x)
            elif self.event == sg.WIN_CLOSED or self.event == 'Quit':
                break
            else:
                qrcode = QR(
                    self.values['caminho'], self.values['coluna'], self.values['diretorio'])
                qrcode.gerarQrcodes()


tela = QrcodeGui()
tela.iniciar()
