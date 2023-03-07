#Overview

Este projeto consiste em uma aplicação em Python que permite a criação de um arquivo PDF de um deck de Magic: The Gathering, a partir de uma URL de sites como: ligaMagic, burnMana, tappedout, moxField (ressalvo que a obtenção do html deste ultimo deve ser manual). O PDF criado contém todas as cartas presentes no deck.

##Instruções de Uso

Para utilizar a ferramenta, é necessário ter o Python 3 instalado no computador, juntamente com as bibliotecas Pillow e requests. Para instalar as bibliotecas, basta executar o seguinte comando:

`pip install -r requirements.txt`

Após a instalação das bibliotecas, basta executar o arquivo proxyCardMTG.py e seguir as instruções apresentadas na tela.

No seu primeiro uso voce pode apenas executar o script init.sh na raiz do projeto e isso  criará um ambiente virtual Python, instalará as dependências necessárias e iniciará a aplicação.

`bash init.sh`

Ao iniciar a aplicação, o usuário terá duas opções:

New: cria um PDF a partir de uma URL de um site compatível.
Old: cria um PDF a partir de um arquivo de deck (.deck).

A aplicação suporta URLs de sites como LigaMagic, BurnMana, TappedOut e MoxField (com algumas limitações).

##Processo

O processo de criação do PDF ocorre em quatro etapas:

Download da página HTML
Extração das cartas presentes no deck
Download das imagens das cartas
Criação do arquivo PDF


O diretório ./deck_{$idDeck} contém todos os metadados do deck, incluindo:

imgs: um diretório com imagens de todas as cartas presentes no deck
{$idDeck}.meta: um arquivo com metadados sobre o site de origem (nome do deck, URL, procedimento de extração e diretório local)
{$idDeck}.deck: um arquivo com metadados sobre o deck (quantidade de cada carta, link da imagem de cada carta e nome de cada imagem)
{$idDeck}.html: um arquivo com o código-fonte estático da página onde o deck está hospedado
{$idDeck}.img: um arquivo com o link de todas as imagens
{$idDeck}.pdf: um arquivo pronto para impressão

Autor
Este projeto foi criado por le314u um viciado em magic e aficionado por commander e legacy.
























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

