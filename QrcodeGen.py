import qrcode
import pandas as pd
import os
from PdfExporter import PDF


class QrcodeGen:
    def __init__(self, caminho, cabecalho, diretorio="Exportado") -> None:
        self.caminho = str(caminho)
        self.cabecalho = cabecalho
        self.diretorio = diretorio
        self.nomes = []

    def criarDiretorio(self, diretorio="Exportado"):
        try:
            os.mkdir(diretorio)
            print("Diretório", diretorio, "Criado com sucesso")
            return os.path.abspath(diretorio)
        except FileExistsError:
            return os.path.abspath(diretorio)

    @staticmethod
    def carregarColunas(arquivo):
        try:
            path = os.path.abspath(arquivo)
            df = pd.read_excel(path)
            colunas = df.columns
            return colunas
        except:
            return {"mensagem": "Falha ao carregar o arquivo !"}

    def carregarPlanilha(self):
        try:
            path = os.path.abspath(self.caminho)
            df = pd.read_excel(path)
            dados = df[self.cabecalho].values
            return dados
        except:
            return {"mensagem": "Falha ao carregar o arquivo !"}

    def gerarQrcodes(self):
        dados = self.carregarPlanilha()
        diretorio = self.criarDiretorio(self.diretorio)

        qr = qrcode.QRCode()
        for x in dados:
            qr = qrcode.QRCode(
                version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=60, border=3)
            qr.add_data(x)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"{diretorio}\{str(x)}.png")
            self.nomes.append((x, f"{diretorio}\{str(x)}.png"))

    def gerarPdf(self):
        pdf = PDF(orientation='L', unit='mm', format=(30, 50))
        pdf.set_font('Arial', '', 8)
        pdf.recebeDados(self.nomes)
        pdf.add_qrcode()
        pdf.output(f"{self.diretorio}/lista.pdf", 'F')
