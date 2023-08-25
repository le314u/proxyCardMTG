from colorama import init, Fore, Back, Style
import os

# É necessário chamar o init() para ativar as sequências de escape ANSI no Windows
init()

def msg(string,val=True):
    line_size = _get_line_size()
    space = ": "
    status_str = "OK" if val else "ERRO"
    colored_status = colored(Fore.GREEN,status_str) if val else colored(Fore.RED, status_str)
    colored_string = colored(Fore.YELLOW,string)
    str_size = len(string) + len(space) + len("status_str")
    cleaner = " " * (line_size - str_size+8) #+2 espaços para cada {} dentro da string formatada
    print(f"{colored_string}{space}{colored_status}{cleaner}")

def colored(color,string):
    return f"{color}{string}{Style.RESET_ALL}"

def _get_line_size():
    terminal_size = os.get_terminal_size()
    return terminal_size.columns 





# Exemplo de impressão de texto colorido
# print(Back.GREEN + "Fundo verde" + Style.RESET_ALL)
# print(Fore.YELLOW + Back.BLUE + "Texto amarelo com fundo azul" + Style.RESET_ALL)
# print(Fore.CYAN + "Texto ciano" + Style.RESET_ALL)
