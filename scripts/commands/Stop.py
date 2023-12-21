import scripts.commands.execute as execute

class Stop():
    def execute(self, option_out):
        execute.command("docker-compose stop")
        input("pressione qualquer tecla para continuar...\n")
        return option_out