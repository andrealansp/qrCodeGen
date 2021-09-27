from re import I, T
from numpy import iinfo
import qrcode
import pandas as pd
from PIL import ImageFont, ImageDraw
import os

documento = ""
cabecalho = ""

# Funcão para checar as informações.


def verificaDados():
    documento = input("Nome da planilha com extensão:")
    cabecalho = input("Cabecalho da planilha a ser usado:")
    try:
        path = os.path.abspath(documento)
        df = pd.read_excel(path)
        dados = df[cabecalho].values
        print(dados)
        return dados
    except:
        verificaDados()

# Criar Diretório.


def criaDiretorio():
    diretorio = "Exportado"
    try:
        os.mkdir(diretorio)
        print("Diretório", diretorio, "Criado com sucesso")
        return os.path.abspath(diretorio)
    except FileExistsError:
        print('Diretório Já Criado')
        return os.path.abspath(diretorio)


caminho = criaDiretorio()
dadosValidados = verificaDados()
qr = qrcode.QRCode()

for x in dadosValidados:
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=60, border=3)
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    fonte = ImageFont.truetype("fonts/verdanab.ttf", 60)
    img_edit = ImageDraw.Draw(img)
    img_edit.text((700, 1490), str(x), "#000", fonte)
    img.save(f"{caminho}\{str(x)}.png")
