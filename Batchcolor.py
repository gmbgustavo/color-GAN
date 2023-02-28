"""
Colorização de imagens em lote usando a API da DeepAI.
"""

import requests
import json
import base64
import os
import yaml
from pathlib import Path


class Batchcolor:

    def __init__(self):
        # Carrega a configuração.
        with open('secret.yaml') as yf:
            config = yaml.load(yf, Loader=yaml.FullLoader)
        self.api_key = config['API_KEY']
        self.url = config['URL']
        self.mask = config['MASK']
        self.bw_images = config['BW_IMAGES']
        self.CONTRAST = config['CONTRAST']
        self.alpha = config['ALPHA']
        self.results_folder = config['RESULTS_FOLDER']

# Carrega os arquivos a serem colorizados
    def read_images(self):
        directory_path = Path(self.bw_images)
        files = []
        for file_path in directory_path.glob('**/*'):
            if file_path.is_file():
                rel_path = file_path.relative_to(directory_path)
                files.append(str(rel_path))
        print(f'\nImagens carregadas: {files[0:3]} e outras {len(files)-4}...\n')
        return files

    def colorize(self, files):
        pass


if __name__ == '__main__':
    # TODO: Add argparse
    batch = Batchcolor()
    lista_imagens = batch.read_images()

    i = 1
    # TODO: Make this a funcion
    for foto in lista_imagens:
        print(f'Imagem {i} de {len(lista_imagens)}: {foto}. Aguarde...')
        with open(foto, 'rb') as f:
            # Converte para base64
            bw_pic = base64.b64encode(f.read()).decode('utf-8')
        # Parametros do request
        data = {'image': bw_pic, 'contrast': CONTRAST, 'alpha': ALPHA}
        # Envia o request para a API
        response = requests.post(URL, headers=headers, data=data)
        # Recebe a resposta em JSON, e isola apenas a URL direta da imagem colorizada
        result_url = json.loads(response.text)['output_url']
        # Faz download da imagem obtida para a pasta de saída
        response = requests.get(result_url)
        filename = os.path.join(RESULTS_FOLDER, os.path.basename(foto))
        with open(filename, 'wb') as f:
            f.write(response.content)
        i += 1

    print(f'\nAs imagens colorizadas foram salvas na pasta {RESULTS_FOLDER}.')

