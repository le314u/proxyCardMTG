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
    #Xor New/Old
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-cmd', action='store_true', help='Roda vida cmd') 
    group.add_argument('-url', help='define qual o url sera extraido o deck')
    group.add_argument('-id', help='define qual o deck sera remontado') 

    self.parser=parser


  def erros(self,cmd):
    if not bool(cmd.url) ^ bool(cmd.id):
      self.parser.error('Deve-se informar apenas um dos argumentos -u ou -id')
      
  def flags(self):
    return self.parser.parse_args()
    
  def config(self):
    cmd = self.parser.parse_args()
    return {"cut" : cmd.cut}
