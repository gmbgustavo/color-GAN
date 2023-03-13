"""
Teste
"""

from PIL import ImageFont, ImageDraw, Image
from pathlib import Path

FONTE = ImageFont.truetype('arial.ttf', 180)
COR = (0, 0, 0)


def carregar(images, text):
    directory_path = Path(images)
    lista_img = []
    texto = ''
    print(f'\nLendo imagens da pasta de origem...')
    for file_path in directory_path.glob('**/*'):
        if file_path.is_file():
            lista_img.append(str(file_path))
    print(f'Total de fotos encontradas: {len(lista_img)}.\n')
    print(f'\nLendo arquivos de texto...')
    directory_path = Path(text)
    for file_path in directory_path.glob('**/*'):
        if file_path.is_file():
            texto = file_path.read_text('UTF-8')
            texto = texto.split(sep='\n\n')
    print(f'Texto OK!\n')
    return lista_img, texto


def _get_center(imagem, texto):
    tam_texto = FONTE.getbbox(texto)
    altura, largura = imagem.size
    x = (largura - tam_texto) / 2
    y = (altura - tam_texto)
    return x, y


def escrever(mangas, texto):
    cont = 0
    for imagem in mangas:
        saida = Image.open(imagem)
        draw = ImageDraw.Draw(saida)
        draw.text((100, 4250), texto[cont], fill=COR, font=FONTE)
        cont += 1
        saida.save('./output_manga/'+str(cont)+'.png')
        print(f'Gravando imagem {cont}...\n')


if __name__ == '__main__':
    imagens, legendas = carregar('./mangas', './legendas')
    escrever(imagens, legendas)


