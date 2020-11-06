import unidecode


lista1="""
1 Trigemeas Sen
1 Tita de Sol
1 Producao Mecanizada
1 Personificador Astuto
1 Nexo do Destino
1 Motor Litoforme
1 Veredito Supremo
1 Silencio
1 Salao da Generosidade de Heliode
1 Ruinas da Academia
1 Retorno de Hurkyl
1 Retorno ao Basico
1 Ressonador Estrionico
1 Relogio Reversor
1 Quebra-cabecas de Teferi
1 Portal de Prototipos
1 Metamorfico Phyrexiano
1 Mandato de Paz
1 Magistrado de Drannith
1 Locutores de Azor
1 Lanterna Cromatica
1 Ladrao de Nocao
1 Imergir em Escuridao
1 Graca do Anjo
1 Fundicao de Almas
1 Fenda Ciclonica
1 Feira dos Inventores
1 Experiencia de Quase-Morte
1 Espelhamento
1 Dia do Julgamento
1 Dizimo Sufocante
1 Conjuracao Dupla
1 Campo Luminominado
1 Colera de Deus
1 Artesaos Feericos
1 Arcanista de Elite
1 Aproximacao do Segundo Sol
1 Ampulheta Purificadora
1 Abolidor-Mor
1 Aco Esculpivel
1 Veto de Dovin
1 Telepatia
1 Talisma da Hierarquia
1 Talisma da Dominacao
1 Ruina Enterrada
1 Propaganda
1 Prisao Fantasmagorica
1 Paisagem Infinita
1 Maniaco do Laboratorio
1 Maga dos Tributos
1 Ilusionista Cefalida
1 Grevas Faiscantes
1 Fabricar
1 Espadas em Arados
1 Descentelhar
1 Cofre de Lim-Dul
1 Cetro Isocrono
1 Cantiga Polinica
1 Caminho para o Exilio
1 Bruma do Paradoxo
1 Aura de Silencio
1 Anel Solar
1 Torre de Comando
1 Sinete Orzhov
1 Sinete Dimir
1 Sinete Azorius
1 Sinete Arcano
1 Sem vestigios
1 Santuario Mistico
1 Reversao Dramatica
1 Remora Mistica
1 Lingote de Aco Negro
1 Estudo Ristico
1 Contramagica
1 Contradicao Arcana
1 Baguncar a Mistura
1 A Pedra Fellwar
8 Planicie
4 Pantano
8 Ilha
1 Elsha do Infinito
1 Visao Ancestral
1 Reservatorio do Fluxo de Eter
1 Redemoinho de Pensamentos
1 Piramide do Panteao
1 Paladino de Aco Puro
1 Pacto de Intervencao
1 Pendulo dos Mentirosos
1 Mochila de Carga
1 Modulo de Animacao
1 Lamina de Lumespectro
1 Insignia de Distincao
1 Incubadora Orochi
1 Holofote Evidenciador
1 Explosivos Fabricados
1 Espada do Grao-Vampiro
1 Elmo dos Deuses
1 Diretriz de Saheeli
1 Desejo da Mente
1 Cornucopia Astral
1 Balancas Seletoras
1 Altar da Linhagem
1 Aglomerado Quimerico
1 Varinha de Vertebras
1 Tudo que Reluz
1 Totem da Avareza
1 Surto Geologico
1 Sopa Quente
1 Sabre Civico
1 Roda Chamejante
1 Retalhos de Asas
1 Reliquia de Aco Negro
1 Polvora Cegante
1 Nevoa Furiosa
1 Mente Eterna
1 Matriz de Pacificacao
1 Martelo do Colosso
1 Mascara de Peregrino
1 Livro de Magicas
1 Garras de Gix
1 Forno da Bruxa
1 Fonte da Renovacao
1 Estrela de Ferro
1 Escudo Triangular
1 Encouracado do Consulado
1 Elixir da Imortalidade
1 Despertar Vulcanico
1 Congelamento Cerebral
1 Chave Voltaica
1 Chave Multipla
1 Cabeca da Gorgona
1 Bolsa do Subornador
1 Bastao de Cristal
1 Vela de Sanguinossebo
1 Urna Dourada
1 Tiro Dispersor
1 Serra Ossea
1 Rede Aranhosa
1 Mina de Gremlin
1 Metralha
1 Mapa da Expedicao
1 Manoplas de Couro de Goblin
1 Magibomba do Voo
1 Magibomba do Panico
1 Machado de Aco Negro
1 Lente da Clareza
1 Lasca-Ossos
1 Lamina de Edro
1 Lamina de Alavanca
1 Khopesh Afiado
1 Jarro de Solda
1 Implemento de Combustao
1 Implemento de Aprimoramento
1 Galho do Andarim
1 Fonte da Juventude
1 Fenda do Solo
1 Esvaziar os Viveiros
1 Espiculo Sismico
1 Esfera Cromatica
1 Escultor de Etherium
1 Escudo dos Concordantes
1 Escudo do Cataro
1 Escopo do Explorador
1 Emplastro de Ervas
1 Cripta de Tormod
1 Casca do Esfolador
1 Carapaca de Cobre
1 Calice do Fluxo Perene
1 Calice de Mana
1 Braceletes Blindados
1 Boleadeiras dos Leoninos
1 Bijuteria do Viajante
1 Bijuteria do Conjurador
1 Bussola do Navegador
1 Aparelhagem de Aventura
1 Aparato Explosivo
1 Oculos do Inventor
3 Ilha
"""


lista2="""
Elsha do Infinito
Pêndulo dos Mentirosos
Mochila de Carga
Insígnia de Distinção
Incubadora Orochi
Diretriz de Saheeli
Desejo da Mente
Altar da Linhagem
Tudo que Reluz
Totem da Avareza
Surto Geológico
Mente Eterna
Livro de Mágicas
Congelamento Cerebral
Chave Múltipla
Esvaziar os Viveiros
Escultor de Etherium
Bijuteria do Viajante
Bijuteria do Conjurador
Trigêmeas Sen
Produção Mecanizada
Nexo do Destino
Motor Litoforme
Salão da Generosidade de Heliode
Retorno de Hurkyl
Retorno ao Básico
Portal de Protótipos
Metamórfico Phyrexiano
Magistrado de Drannith
Lanterna Cromática
Feira dos Inventores
Experiência de Quase-Morte
Espelhamento
Dia do Julgamento
Dízimo Sufocante
Conjuração Dupla
Campo Luminominado
Artesãos Feéricos
Ampulheta Purificadora
Abolidor-Mor
Aço Esculpível
Veto de Dovin
Talismã da Hierarquia
Talismã da Dominação
Prisão Fantasmagórica
Paisagem Infinita
Maga dos Tributos
Ilusionista Cefálida
Espadas em Arados
Descentelhar
Cofre de Lim-Dûl
Cantiga Polínica
Bruma do Paradoxo
Sinete Orzhov
Sinete Dimir
Sinete Arcano
Sem vestígios
Santuário Místico
Reversão Dramática
Rêmora Mística
Estudo Rístico
Contramágica
Contradição Arcana
Bagunçar a Mistura
A Pedra Fellwar
Planície
"""


def vet(lista):
    new = lista.replace("1 ","")
    new = unidecode.unidecode(new)
    return new.split('\n')


def complemento(listaOn,listaOff):
    for item in listaOff:
        try:
            listaOn.remove(item)
        except:
            pass
        
    return listaOn

def pretty(newList):
    for item in newList:
        print("1 "+item)

newList=complemento(vet(lista1),vet(lista2))
pretty(newList)
