# Overview

Este projeto consiste em uma aplicação em Python que permite a criação de um arquivo PDF de um deck de Magic: The Gathering, a partir de uma URL de sites como: ligaMagic, burnMana, tappedout, moxField (ressalvo que a obtenção do html deste ultimo deve ser manual). O PDF criado contém todas as cartas presentes no deck.

## Instalação

Para utilizar a ferramenta, é necessário ter o Python 3 instalado no computador, juntamente com as bibliotecas Pillow e requests. Para instalar as bibliotecas, basta executar o seguinte comando:

```pip install -r requirements.txt```

Após a instalação das bibliotecas, basta executar o arquivo proxyCardMTG.py e seguir as instruções apresentadas na tela.

No seu primeiro uso voce pode apenas executar o script init.sh na raiz do projeto e isso  criará um ambiente virtual Python, instalará as dependências necessárias e iniciará a aplicação.

```bash init.sh```

## Instruções de Uso

Ao iniciar a aplicação, o usuário terá duas opções:

| Opção  | Descrição                                               |
|--------|:--------------------------------------------------------:|
| New    | Cria um PDF a partir de uma URL de um site compatível.   |
| Old    | Cria um PDF a partir de um arquivo de deck (.deck).      |

A opção `new` suporta URLs de sites como LigaMagic, BurnMana, TappedOut e MoxField (com algumas limitações pois a captura do html do mox field deve ser feita manualmente).

### Processo

O processo de criação do PDF ocorre em quatro etapas:

Download da página HTML  
Extração das cartas presentes no deck  
Download das imagens das cartas  
Criação do arquivo PDF  

### Estrutura
O diretório ./deck_{$idDeck} contém todos os metadados do deck, incluindo:

| Arquivo/Diretorio | Descrição |
| --- | --- |
| imgs/ | Um diretório com imagens de todas as cartas presentes no deck |
| {$idDeck}.meta | Um arquivo com metadados sobre o site de origem (nome do deck, URL, procedimento de extração e diretório local) |
| {$idDeck}.deck | Um arquivo com metadados sobre o deck (quantidade de cada carta, link da imagem de cada carta e nome de cada imagem) |
| {$idDeck}.html | Um arquivo com o código-fonte estático da página onde o deck está hospedado |
| {$idDeck}.img | Um arquivo com o link de todas as imagens |
| {$idDeck}.pdf | Um arquivo pronto para impressão |


### Autor
Este projeto foi criado por le314u um viciado em magic e aficionado por commander e legacy.


