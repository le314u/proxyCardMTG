# Pega a url
from modulos import extraction, pdf, persistence, request
from ast import literal_eval

url = input("Digite a url: ")
persistence = persistence.persistence()
request = request.request()
extract = extraction.extraction("oi")
pdf = pdf.pdf()


#Pega dados essenciais da URL
persistence.processeUrl(url)


#Verifica se existe um diretorio proprio para o deck
if not persistence.it_is_ok(persistence.pastaDeck):
    #Cria o diretorio que ficara todos os arquivos do deck
    if(not persistence.persistDir(persistence.pastaDeck)):
        print("Erro ao criar Diretorio")

#Request da Pagina
if(not persistence.processOk("html")):
    #Faz Download da pagina 
    html = request.downloadHTML(url)
    #Persiste a pagina 
    persistence.persistFile(html, "html")
else:
    #Le o html do arquivo
    html = persistence.load("html")

#Cataloga o Deck
if(not persistence.processOk("deck")):
    #Preparando para trabalhar com o deck
    extract.load(html, persistence.nameDeck, persistence.pastaDeck)
    #Cataloga o Deck
    deck = extract.catalogarDeck()
    #Persiste o Deck 
    persistence.persistFile(str(deck), "deck")
else:
    #Le o arquivo de catalogo do Deck
    deck = literal_eval(persistence.load("deck"))

#Faz Download das Imagens
if(not persistence.processOk("img") or persistence.persistDir(persistence.pastaDeck+"/imgs") ):
    #Cria uma pasta para persistir as imagens
    persistence.persistDir(persistence.pastaDeck+"/imgs/")
    urlCards = ''
    #Preparando para trabalhar com o deck
    for type in deck:
        for card in deck[type]:
            urlCards = urlCards + card['url']+'\n'
            #Faz Download da imagem
            request.downloadIMG("https://"+card['url'], persistence.pastaDeck+"/imgs/"+card['img']+'.jpg')
    persistence.persistFile(urlCards, "img")

#Cria o Pdf
if(not persistence.processOk("pdf")):
    #Preparando para trabalhar com o deck

    #Cria o canvas do PDF
    pdf.makePdf(persistence.pastaDeck+"/"+persistence.nameDeck+".pdf")

    #Preenche o canvas com as imagens do Deck
    for type in deck:
        for card in deck[type]:
            for i in range(card['qtd']):
                pdf.printCard(persistence.pastaDeck+"/imgs/"+card['img']+'.jpg')
    pdf.close()



