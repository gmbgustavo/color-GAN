# color-GAN
Restauração e colorização de fotos antigas
Esse script usa a API do DeepAI, que é um serviço pago, para colorização de arquivos em lote.


## Parâmetros do config.yaml

API_KEY: A sua API

URL: O endereço de conexão do DeepAI (padrão 'https://api.deepai.org/api/colorizer')

MASK: Pode ser usado para fazer colorização guiada de uma foto através de uma máscara. Indicar o caminho da imagem de máscara.

BW_IMAGES: O caminho das imagens em preto e branco.

CONTRAST: Contraste da colorização

ALPHA: Nível alpha da colorização.

RESULTS_FOLDER: Onde serão salvos os arquivos colorizados.

