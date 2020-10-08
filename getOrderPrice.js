function linhaValid(linha){
    return linha.getElementsByTagName("td").length == 4
}
function qtd(linha){
    return linha.getElementsByTagName("td")[0].innerText
}
function valor(linha){
    return linha.getElementsByTagName("td")[3].innerText.replace(',','.')
}
function nome(linha){
    return linha.getElementsByTagName("td")[1].innerText
}


Deck = document.getElementsByClassName("pdeck-block")[0]
tbody = Deck.getElementsByTagName("tbody")[0]
linhas = tbody.getElementsByTagName("tr")

cards = []
for (let linha of linhas){
    if(linhaValid(linha)){
        cards.push([valor(linha),nome(linha)])
        //console.log(valor(linha),";",nome(linha))
    }
}



function comparar(a, b) {
  newA = parseFloat(a[0])
  newB = parseFloat(b[0])
  if(newA < newB) {
    return -1;
  }
  if(newA > newB) {
    return 1;
  }
  return 0;
}

cards.sort(comparar)

newString = ""
for(let card of cards){
  newString = newString + card[0] + " " + card[1] + "\n"
  //console.log('1 ',card[1])
}
console.log(newString)
