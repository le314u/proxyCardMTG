A partir de uma url para um deck será criado um pdf pronto para impressão das proxy de MTG

## Como fazer

Ao executar o comando

> ./init.sh

Será aberto o programa dentro de um ambiente virtual.
Será isntalada todas as depêndencias
Será requisitado uma url do site liga magic ou burn mana como por exemplo

>ligaMagic

>burnMana

>tappedout

>moxField (Problemas para fazer download do HTML)


será feito downlaod de todas as artes das cartas que compoẽ deck principal e colocadas em ./deck_***$id*** onde tambem  estará o arquivo pdf que contem todas as cartas prontas para impressão para jogar *For fun*

### Estrutura

Será criado o seguintes diretorios:

├── <$id>.meta
├── <$id>.html
├── <$id>.deck
├── <$id>.img
├── <$id>.pdf
└── imgs


Sendo:

imgs diretorio com todas as imagen de todos os cards presente no deck

<$id>.meta arquivo com meta dados sobre o site de origem (nome do deck, url, procedimento de extração, dirLocal)

<$id>.deck arquivo com meta dados sobre o deck (quantidade da carta presente no deck, link da imagem de cada carta, nome de cada imagem)

<$id>.html download do codigo fonte estático da pagina onde está hospedado o deck

<$id>.img arquivo com o link de todas as imagens

<$id>.pdf arquivo pronto para impressão


