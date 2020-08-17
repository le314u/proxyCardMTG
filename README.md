A partir de uma url para um deck será criado um pdf pronto para impressão das proxy de MTG

## Como fazer

Ao executar o comando

> ./init.sh

Será aberto o programa dentro de um ambiente virtual.
Será isntalada todas as depêndencias
Será requisitado uma url do site liga magic ou burn mana como por exemplo

>https://www.ligamagic.com.br/?view=dks/deck&id=872745

sendo o $id = 872745

>https://burnmana.com/decks/pioneer/azorius/1595169623289

sendo o $id = 1595169623289

será feito downlaod de todas as artes das cartas que compoẽ deck principal e colocadas em ./deck_***$id*** onde tambem  estará o arquivo pdf que contem todas as cartas prontas para impressão para jogar *For fun*


Será criado o seguintes diretorios:

├── <$id>.deck

├── <$id>.html

├── <$id>.img

├── <$id>.pdf

└── imgs


Sendo:
<$id>.deck arquivo com meta dados sobre o deck (quantidade da carta presente no deck, link da imagem de cada carta, nome de cada imagem)

<$id>.html download do codigo fonte estático da pagina onde está hospedado o deck

<$id>.img arquivo com o link de todas as imagens

<$id>.imgs diretorio com todas as imagen de todos os cards presente no deck

<$id>.pdf arquivoi pronto para impressão


