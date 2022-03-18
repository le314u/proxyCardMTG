import os

deck = {"Tokens": []}

pasta = './'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        deck["Tokens"].append( {"qtd": 1,"name": "token_"+arquivo,"url": "repositorio","img": arquivo} );

f=open("token.deck", 'w+')
f.write(deck)
