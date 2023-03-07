import argparse

parser = argparse.ArgumentParser(
  prog = 'proxyMTG',
  description =  'Este é um projeto Python que gera um arquivo PDF de um deck de Magic: The Gathering. A partir de uma URL de sites como ligaMagic, burnMana, tappedout e moxField',
  epilog = 'Seja combeiro mas nunca seja safado ;)')
                    
#Flag
parser.add_argument('-cut', action='store_true', help='imprime a borda da carta') 
#Xor New/Old
group = parser.add_mutually_exclusive_group()
group.add_argument('-cmd', action='store_true', help='Roda vida cmd') 
group.add_argument('-u', '--url', help='define qual o url sera extraido o deck')
group.add_argument('-id', help='define qual o deck sera remontado') 



cmd = parser.parse_args()
config = {"cut" : cmd.cut}

# Erros
if not bool(cmd.url) ^ bool(cmd.id):
    parser.error('Deve-se informar apenas um dos argumentos -u ou -id')
    
#Fluxo
if bool(cmd.url):
  pass
if bool(cmd.id):
  pass
  
