import os

class Menu:
    
    def __init__(self):
        pass

    def display(self, dict):
        """ Mostra as opções possiveis """
        for chave in dict.keys():
            print("["+chave+"] " + dict[chave])
    
    def option(self, dict, arg):
        """ Verifica se a opção é valida """
        try:
            dict[arg]
            return True
        except:
            return False

    def selection(self, dict):
        """ Opções do menu """
        os.system('clear') or None
        while(True):
            # Mostra as opções
            self.display(dict)
            # Recebe uma opção
            arg = input("Digite a opção: ")
            condition = self.option(dict, arg)
            #Valida a opção
            if condition : break 
            else:
                os.system('clear') or None
        return arg