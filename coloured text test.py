from colorama import init as colorama_init
from colorama import Fore, Back, Style

colorama_init()



print(f"{Fore.RED}hellow")
print(f"{Fore.YELLOW}hellow")
print(f"{Fore.BLUE}hellow")
print(f"{Fore.GREEN}████████████████████████████")
print(f"{Fore.WHITE}hellow")
print(f"{Fore.BLACK}hellow")
print(f"{Fore.YELLOW}hellow")
print(f"{Fore.RED}hellow")
print(f"{Fore.RED}hellow")

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')