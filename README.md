# Overview

Este projeto consiste em uma aplicação em Python que permite a criação de um arquivo PDF de um deck de Magic: The Gathering, a partir de uma URL de sites como: ligaMagic, burnMana, tappedout, moxField (ressalvo que a obtenção do html deste ultimo deve ser manual). O PDF criado contém todas as cartas presentes no deck.

## Instalação

Para utilizar a ferramenta, é necessário ter o Python 3 instalado no computador e baixar as dependências em  requirements.txt por meio do comando:

```pip install -r requirements.txt```

Após a instalação das bibliotecas, basta executar o arquivo proxyCardMTG.py e seguir as instruções apresentadas na tela.

No seu primeiro uso voce pode apenas executar o script init.sh na raiz do projeto e isso  criará um ambiente virtual Python, instalará as dependências necessárias e iniciará a aplicação.

```bash init.sh```

## Instruções de Uso

O programa suporta URLs de sites como LigaMagic, BurnMana, TappedOut e MoxField (com algumas limitações pois a captura do html do mox field deve ser feita manualmente).


## Comandline

O projeto possui um conjunto de opções de linha de comando para personalizar o processo de geração do PDF do deck. Aqui estão algumas das opções disponíveis:

- `-url`: Define a URL da qual o deck será extraído.
- `-id`: Define o ID do deck a ser remontado.


- `-cut`: Imprime a borda da carta. [INATIVA]
- `-i`: Inicia o modo interativo do menu.[INATIVA]
- `-html`: Força o request da página HTML.[INATIVA]
- `-e` ou `--extract`: Força a extração de dados do HTML.[INATIVA]
- `-d`: Força o download das imagens.[INATIVA]
- `-pdf`: Força apenas a reescrita do PDF.[INATIVA]


### Processo

O processo de criação do PDF ocorre em cinco etapas:
Criação de um arquivo que preserva MetaDados
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


