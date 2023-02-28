# color-GAN
Restauração e colorização de fotos antigas
Esse script usa a API do DeepAI, que é um serviço pago, para colorização de arquivos em lote.


## config.yaml

API_KEY: 'YOUR DEEP AI API KEY' - A sua API

URL: 'https://api.deepai.org/api/colorizer' - O endereço de conexão do DeepAI

MASK: '' - Pode ser usado para fazer colorização guiada de uma foto através de uma máscara.

BW_IMAGES: './originals/' - O caminho das imagens em preto e branco.

CONTRAST: 2 - Contraste da colorização

ALPHA: 0.65 - Nível alpha da colorização.

RESULTS_FOLDER: './results/' - Onde serão salvos os arquivos colorizados.

