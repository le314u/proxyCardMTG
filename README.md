# proxyCardMTG
A partir de uma url para um deck, será criado um pdf pronto para impressão das proxy de MTG

## Como fazer

Ao executar o comando *./init.sh*
 
Será aberto o programa dentro de um ambiente virtual, instalado todas as depêndencias e iniciará a aplicação.

Ao iniciar a aplicação há duas opçoes 
1. Old (Recria o pdf a partir de <$id>.deck)
2. New (Cria um pdf a partir de uma URL)

A aplicação aceita url do seguintes sites:

- ligaMagic
- burnMana
- tappedout
- moxField (Problemas para fazer download do HTML)

O processo para criação do PDF é:

1. Download da pagina HTML
2. Extração das cartas presentes no Deck
3. Download das imagens
4. Criação do PDF

Todos os metadados do deck são colocados em ./deck_***$id*** 

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

