"""
Colorização de imagens em lote usando a API da DeepAI.
O uso da API da DeepAI é cobrado na conta do utilizador, 
que deve informar sua chave API única para poder acessar.
Mantenha sua chave em sigilo.
Os parâmetros devem ser informados no arquivo config.yaml.
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
        try:
            with open('secret.yaml') as yf:
                config = yaml.load(yf, Loader=yaml.FullLoader)
        except FileNotFoundError:
            print("O arquivo de configuração (config.yaml) não foi encontrado.")
        self.api_key = config['API_KEY']
        self.url = config['URL']
        self.mask = config['MASK']
        self.bw_images = config['BW_IMAGES']
        self.contrast = config['CONTRAST']
        self.alpha = config['ALPHA']
        self.results_folder = config['RESULTS_FOLDER']

    # Carrega os arquivos a serem colorizados
    def _read_images(self):
        directory_path = Path(self.bw_images)
        files = []
        nomes = []
        print(f'\nLendo imagens da pasta de origem...')
        for file_path in directory_path.glob('**/*'):
            if file_path.is_file():
                files.append(str(file_path))
                nomes.append(str(file_path.relative_to(directory_path)))
        print(f'Total de fotos encontradas: {len(files)}.\n({nomes[0:2]} e mais {len(files)-4}) \n')
        return files

    def colorize(self):
        lista_imagens = self._read_images()
        headers = {'api-key': self.api_key}
        data = {'image': None, 'contrast': self.contrast, 'alpha': self.alpha}
        i = 1    # Simple counter
        option = input('Deseja continuar? (S/N)')
        if option.lower() == 's':
            for foto in lista_imagens:
                print(f'Colorizando foto {i} de {len(lista_imagens)}: {foto}. Aguarde...')
                with open(foto, 'rb') as f:
                    # Converte para base64
                    bw_pic = base64.b64encode(f.read()).decode('utf-8')
                # Parametros do request
                data['image'] = bw_pic
                # Envia o request para a API
                response = requests.post(self.url, headers=headers, data=data)
                # Recebe a resposta em JSON, e isola apenas a URL direta da imagem colorizada
                result_url = json.loads(response.text)['output_url']
                # Faz download da imagem obtida para a pasta de saída
                response = requests.get(result_url)
                filename = os.path.join(self.results_folder, os.path.basename(foto))
                with open(filename, 'wb') as f:
                    f.write(response.content)
                i += 1
            print(f'\nAs imagens colorizadas foram salvas na pasta {self.results_folder}.')
        else:
            quit()


if __name__ == '__main__':
    batch = Batchcolor()
    batch.colorize()
