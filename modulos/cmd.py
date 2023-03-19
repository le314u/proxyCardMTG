import argparse

class CMD:
  def __init__(self):
    print("OK")
    parser = argparse.ArgumentParser(
      prog = 'proxyMTG',
      description =  'Este é um projeto Python que gera um arquivo PDF de um deck de Magic: The Gathering. A partir de uma URL de sites como ligaMagic, burnMana, tappedout e moxField',
      epilog = 'Seja combeiro mas nunca seja safado ;)')
                        
    #Flag
    parser.add_argument('-cut', action='store_true', help='imprime a borda da carta') 
      #Forçar downlaod das imagens novamente
    #Xor New/Old
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', action='store_true',default=False, help='Menu interativo') 
    group.add_argument('-url', help='define qual o url sera extraido o deck')
    group.add_argument('-id', help='define qual o deck sera remontado') 
    #Continua de uma determinada etapa
    step = parser.add_mutually_exclusive_group()
    step.add_argument('-html', action='store_false', help='Força o request da pagina html') 
    step.add_argument('-e',"--extract", action='store_false', help='Força a extração de dados do HTML') 
    step.add_argument('-d', action='store_false', help='Força o download das imagens') 
    step.add_argument('-pdf', action='store_false', help='Força apenas a reescrita do PDF') 
  
    self.parser=parser


  def erros(self,cmd):
    if not bool(cmd.url) ^ bool(cmd.id):
      self.parser.error('Deve-se informar apenas um dos argumentos -u ou -id')
      
  def flags(self):
    return self.parser.parse_args()
    
  def config(self):
    cmd = self.parser.parse_args()
    return {"cut" : cmd.cut}
