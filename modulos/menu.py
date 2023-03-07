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

    def input(self):
        return input("-"*40 +"\nDigite a opção: ")

    def selection(self, dict):
        """ Opções do menu """
        os.system('clear') or None
        count = 0
        while(True):
            # Mostra as opções
            self.display(dict)
            #Valida a opção
            arg = self.input()
            if self.option(dict, arg) : break 
            else:
                count=count+1;
                if count >=3:
                    self.error()
                os.system('clear') or None
        return arg

    def error(self):
        print("-"*40)
        print("Estou presumindo que você não esta lendo, entao vou encerrar")
        print("-"*40)
        exit()
