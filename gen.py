from re import I
import qrcode
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import os

data = {}
path = os.path.abspath("dados2.xlsx")
df = pd.read_excel(path)

pessoas = df['Nº pess.'].values
qr = qrcode.QRCode()


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

for x in pessoas:
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=60, border=3)
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    fonte = ImageFont.truetype("fonts/verdanab.ttf", 10)
    img_edit = ImageDraw.Draw(img)
    img_edit.text((10, 60), "World", (0, 0, 0, 255), fonte)
    img.save(f"{caminho}\{str(x)}.png")
