from .commands.Build import Build
from .commands.Start import Start
from .commands.Stop import Stop
from .commands.Restart import Restart
from .commands.Clean import Clean
from .commands.Ps import Ps
from .commands.Rm import Rm
from .commands.Backup import Backup
from .commands.Sair import Sair

class Menu:
    # Atributo da classe
    opcoes = [
        {
            "title": "build",
            "function": Build()
        },
        {
            "title": "start",
            "function": Start()
        },
        {
            "title": "stop",
            "function": Stop()
        },
        {
            "title": "restart",
            "function": Restart()
        },
        {
            "title": "clean",
            "function": Clean()
        },
        {
            "title": "ps",
            "function": Ps()
        },
        {
            "title": "rm",
            "function": Rm()
        },
        {
            "title": "backup",
            "function": Backup()
        },
        {
            "title": "sair",
            "function": Sair()
        }
    ]

    def __init__(self):
        self.size_opcoes = len(self.opcoes)

    def print_menu(self):
        print("Menu do servidor:")
        for index, opcao in enumerate(self.opcoes):
            print(f"{index + 1}. {opcao['title']}")

    def error_msg(self):
        print("Escolha as opções listadas")

    # Método da classe
    def execute(self):
        num_opcao = -1
        while(num_opcao != 0):
            self.print_menu()
            num_opcao = self.get_opcao()
            if(not(num_opcao >= 0 and num_opcao <= self.size_opcoes-1)):
                self.error_msg()
                continue
            opcao_selecionada = self.opcoes[num_opcao]
            num_opcao = opcao_selecionada['function'].execute(num_opcao)
            num_opcao = (num_opcao + 1) % len(self.opcoes)
    
    def get_opcao(self) -> int:
        while True:
            try:
                return int(input("Selecione o número da opção desejada: ")) - 1
            except ValueError:
                self.error_msg()
                self.print_menu()
                print("")